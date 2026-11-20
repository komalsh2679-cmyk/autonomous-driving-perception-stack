# Implementation notes (local changes)

## Changes in this version

- Fixed the default input path to the sample image included in `assets/sample_images/`.
- Added selectable Ultralytics ByteTrack tracking for video/webcam runs. The original local tracker remains available as `tracker_backend: custom`.
- Added an optional MiDaS-small relative-depth heatmap. It is disabled by default; enable it using `depth.enabled: true` in `config/settings.yaml`.
- Changed stream output saving from individual JPEG frames to one annotated MP4 file.
- Added Windows CPU setup, run, and test batch files.
- Kept the existing steering/throttle/brake modules and the original sample project structure.

## Important limits

- The default sample is a single still image. ByteTrack's temporal tracking should be demonstrated with a video or webcam, not a single image.
- MiDaS depth is relative and is not calibrated distance in metres. Existing bounding-box-based range values are only rough approximations.
- This repository does not implement training/fine-tuning, BDD100K/KITTI analysis, lane-segmentation comparison, CARLA/ROS2, ONNX/TensorRT benchmarking, or W&B logging yet.
- The included `LICENSE` file contains unresolved conflict markers and mixed license text. Verify the upstream license and replace it with a valid license file before redistributing the modified repository publicly. This change intentionally does not guess which license was intended.
- Run the full demo on the target computer after installing dependencies; passing unit tests alone does not prove the model-download or full perception pipeline works there.

## Quick run

1. Run `setup_windows_cpu.bat` once on Windows.
2. Run `run_demo.bat`.
3. To save output, set `input.save_outputs: true` in `config/settings.yaml`.
4. To enable MiDaS, set `depth.enabled: true` (requires internet on first load).
5. Run `run_tests.bat` or `python -m pytest -q`.
