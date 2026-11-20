"""Optional MiDaS relative-depth visualization.

MiDaS output is relative depth, not calibrated distance in metres. The
module imports PyTorch lazily so the normal pipeline does not pay the model
loading/download cost unless depth.enabled is turned on.
"""

from __future__ import annotations

import cv2
import numpy as np


class MiDaSDepthEstimator:
    """Generate a colourized relative-depth map with a small MiDaS model."""

    def __init__(self, model_type: str = "MiDaS_small", device: str = "auto") -> None:
        try:
            import torch
        except ImportError as exc:  # pragma: no cover - depends on local environment
            raise ImportError(
                "MiDaS depth needs PyTorch. Install the project's requirements first."
            ) from exc

        if device == "auto":
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.device = torch.device(device)

        try:
            # First run may download the MiDaS repo and model weights through Torch Hub.
            self.model = torch.hub.load("intel-isl/MiDaS", model_type, trust_repo=True)
            transforms = torch.hub.load("intel-isl/MiDaS", "transforms", trust_repo=True)
        except Exception as exc:  # pragma: no cover - external download/model cache
            raise RuntimeError(
                "Could not load MiDaS from Torch Hub. Check your internet connection, "
                "then retry; depth estimation is optional and can remain disabled."
            ) from exc

        if model_type.lower().endswith("small"):
            self.transform = transforms.small_transform
        else:
            self.transform = transforms.dpt_transform
        self.model.to(self.device).eval()
        self._torch = torch

    def predict(self, image_bgr: np.ndarray) -> np.ndarray:
        """Return a BGR heatmap whose colours represent relative depth only."""
        if image_bgr is None or image_bgr.size == 0:
            raise ValueError("MiDaS received an empty image")
        torch = self._torch
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        batch = self.transform(image_rgb).to(self.device)
        with torch.no_grad():
            prediction = self.model(batch)
            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=image_bgr.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()
        relative = prediction.detach().cpu().numpy().astype(np.float32)
        finite = np.isfinite(relative)
        if not finite.any():
            raise RuntimeError("MiDaS returned no finite depth values")
        low, high = np.percentile(relative[finite], [2, 98])
        normalized = np.zeros(relative.shape, dtype=np.uint8)
        if high > low:
            scaled = np.clip((relative - low) / (high - low), 0.0, 1.0)
            scaled[~finite] = 0.0
            normalized = (scaled * 255).astype(np.uint8)
        # MiDaS is an inverse-depth estimate in typical checkpoints; the map is for visualization.
        return cv2.applyColorMap(normalized, cv2.COLORMAP_MAGMA)
