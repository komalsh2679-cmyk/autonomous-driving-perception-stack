from pathlib import Path

from config.config import load_config


def test_load_config() -> None:
    config = load_config("config/settings.yaml")
    assert config.input.image_width == 1280
    assert "person" in config.detection.target_classes
    assert config.detection.tracker_backend == "bytetrack"
    assert config.depth.enabled is False
    assert Path(config.input.source).is_file()
