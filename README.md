# Autonomous Driving Perception Stack Using Machine Learning

**Internship Project – Nexvia Technologies**  
**Domain:** Machine Learning / Computer Vision

## 1. Project Overview

This project implements a computer vision-based autonomous driving perception prototype using Python, YOLOv8 and OpenCV.

The system processes road images and video footage to identify road users, track detected objects, estimate approximate distances, detect lane markings and classify potential risks.

The project is designed to run on CPU-based computers and provides annotated visual outputs for demonstrating the perception pipeline.

CARLA simulator integration is considered future work. The current implementation can be tested using images and recorded videos without requiring a CARLA installation.

## 2. Project Objectives

- Detect vehicles, pedestrians and other road objects.
- Track detected objects and assign tracking IDs.
- Estimate approximate distances from detected objects.
- Identify object positions within the camera frame.
- Detect road lane markings using OpenCV.
- Classify potential risks into LOW, MEDIUM and HIGH.
- Generate annotated image and video outputs.
- Develop and test a modular Python-based perception pipeline.

## 3. Implemented Features

### Object Detection
- YOLOv8-based object detection using the Ultralytics framework.
- Identifies supported road-related object classes.
- Displays bounding boxes, class labels and confidence scores.

### Object Tracking
- Assigns tracking IDs to detected objects in video streams.
- Supports tracking across consecutive frames.
- Provides object identity information for the perception pipeline.

### Lane Detection
- OpenCV-based lane detection.
- Image preprocessing and grayscale conversion.
- Gaussian blur and Canny edge detection.
- Region of interest selection.
- Hough line detection and lane visualization.

### Approximate Distance Estimation
- Uses detected bounding-box information to estimate approximate object distance.
- Displays object position, distance and associated risk information.
- Distance values are approximate and are not calibrated ground-truth measurements.

### Risk Classification
- Classifies detected objects into LOW, MEDIUM and HIGH risk categories.
- Uses estimated distance and object-related information to support risk assessment.

### Image and Video Processing
- Supports road image and video inputs.
- Displays detection and perception information.
- Generates annotated visual outputs.
- Supports CPU-based execution.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.10 | Main programming language |
| YOLOv8 | Object detection |
| OpenCV | Image, video and lane processing |
| NumPy | Numerical operations |
| Ultralytics | YOLO model framework |
| PyTorch | Deep learning framework |
| PyYAML | Configuration management |
| Pytest | Automated testing |

## 5. System Architecture

The perception pipeline follows this workflow:

```text
        Image / Video Input
                 |
                 v
        Image Preprocessing
                 |
          +------+------+
          |             |
          v             v
     Lane Detection  Object Detection
       (OpenCV)        (YOLOv8)
          |             |
          |             v
          |        Object Tracking
          |             |
          |             v
          |      Distance Estimation
          |             |
          |             v
          |       Risk Classification
          |             |
          +------+------+
                 |
                 v
          Annotated Output
           Image / Video
```

## 6. Project Folder Structure

```text
Autonomous-Driving-CARLA/
│
├── config/
│   └── settings.yaml
│
├── assets/
│   ├── sample_images/
│   ├── sample_videos/
│   └── outputs/
│
├── src/
│   ├── main.py
│   └── perception modules
│
├── tests/
│
├── docs/
│
├── requirements.txt
├── setup_windows_cpu.bat
├── run_demo.bat
├── README.md
└── ARCHITECTURE.md
```

The exact files and additional modules are available in the repository.

## 7. Installation and Setup

### Requirements
- Windows 10 or Windows 11.
- Python 3.10.
- Internet connection for initial dependency and model downloads.
- Sufficient disk space for Python packages and model weights.

### Setup

Run the Windows CPU setup script:

```powershell
.\setup_windows_cpu.bat
```

Alternatively, install the dependencies manually:

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 8. Running the Project

Open the terminal in the project root directory.

### Run the default image demo

```powershell
.\run_demo.bat
```

The default image source is configured in:

```text
config/settings.yaml
```

### Run the video demo

Edit the input source in `config/settings.yaml`:

```yaml
input:
  source: assets/sample_videos/traffic.mp4
```

Then execute:

```powershell
.\run_demo.bat
```

The first YOLOv8 execution may download the required model weights. An internet connection is required if the weights are not already available locally.

### Run automated tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## 9. Testing and Results

The project was tested using image and video inputs in a Windows CPU-based environment.

Verified functional results:

- Image processing executed successfully.
- Video processing executed successfully.
- Object detection bounding boxes and labels were displayed.
- Tracking IDs were displayed on detected objects.
- Approximate distance information was generated.
- Risk classifications were displayed.
- Annotated video output was generated.

### Automated Testing

**Previous verified test run:**
- Total tests passed: 11
- Execution time: 6.86 seconds

These are functional test results, not model accuracy or real-time performance measurements.

## 10. Hardware and Performance Considerations

The project was configured for CPU-based execution without requiring an NVIDIA GPU.

YOLOv8 inference speed depends on the processor, input resolution and number of detected objects. CPU processing may be slower than GPU-based inference.

The distance estimation module provides approximate values and should not be considered a calibrated safety measurement.

## 11. Limitations and Future Improvements

The current project is a perception prototype. Further development can include:

- Training and fine-tuning YOLOv8 on BDD100K or KITTI datasets.
- Dataset exploration and class-balance analysis.
- Evaluating object detection using precision, recall and mAP.
- Comparing classical lane detection with a lane segmentation model.
- Evaluating MiDaS or other depth-estimation approaches.
- Integrating the perception pipeline with the CARLA simulator.
- Adding ROS2 communication.
- Exporting models to ONNX and benchmarking inference.
- Exploring TensorRT optimization on supported NVIDIA hardware.
- Integrating Weights & Biases for experiment tracking.

These items are proposed improvements and are not claimed as completed features.

## 12. Individual Learning Outcomes

This internship project provided practical experience in:

- Python-based computer vision development.
- YOLOv8 object detection.
- Object tracking in video streams.
- Image and video processing using OpenCV.
- Lane detection techniques.
- Approximate distance estimation and risk classification.
- Debugging, dependency management and automated testing.
- Building a modular perception pipeline under limited hardware resources.

## 13. Acknowledgements

Developed as part of the Machine Learning internship at Nexvia Technologies.

## 14. License and Attribution

Review the original repository's license and preserve appropriate third-party attribution before redistributing the modified code. Do not claim ownership of third-party components.
