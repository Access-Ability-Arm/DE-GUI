# DE-GUI

AI-powered GUI for the Drane Engineering assistive robotic arm, featuring real-time object detection, face tracking, and depth sensing.

## Features

- **YOLOv11 Object Detection**: Real-time segmentation with Apple Metal GPU acceleration
- **Face Tracking**: 20-point facial landmark detection with MediaPipe
- **Depth Sensing**: Intel RealSense support for distance measurement (optional)
- **Flexible Camera Support**: Auto-detects RealSense, webcams, or Continuity Camera
- **Manual Controls**: Direct robotic arm control (x, y, z, grip)
- **Toggle Modes**: Press 'T' to switch between face tracking and object detection

## Quick Start

### Installation

See [docs/installation.md](docs/installation.md) for detailed setup instructions.

**Quick version:**
```bash
# Create virtual environment with Python 3.11
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
source venv/bin/activate  # Activate virtual environment
python main.py
```

The application will automatically:
- Detect available cameras (RealSense → webcam → Continuity Camera)
- Enable GPU acceleration (Apple Metal, CUDA, or CPU)
- Download YOLOv11 model on first run (~6MB)

### Controls

- **Camera Selection**: Choose camera from dropdown menu
- **Detection Mode**: Press 'T' to toggle between face tracking and object detection
- **Robotic Arm**: Use GUI buttons for manual control (x±, y±, z±, grip)

## System Requirements

- **Python**: 3.11 (required - MediaPipe does not support 3.14+)
- **Camera**: Any webcam, or Intel RealSense D400-series for depth sensing
- **OS**: macOS, Windows, or Linux
- **GPU** (optional): Apple Silicon (Metal), NVIDIA (CUDA), or CPU

## Detection Modes

### Object Detection (Default)
- Detects and segments 80 COCO object classes
- Real-time bounding boxes and colored masks
- Distance measurement with RealSense camera
- Fixed reference point depth indicator

### Face Tracking
- 20 mouth landmark points using MediaPipe
- Center point calculation and visualization
- Works with any standard webcam

## Architecture

The application uses a modular architecture for maintainability:

```
access-ability-arm/
├── config/       # Configuration & feature detection
├── gui/          # PyQt6 main window & UI
├── hardware/     # Camera & button controllers
├── vision/       # Computer vision (YOLO, face detection)
├── workers/      # Image processing thread
└── main.py       # Application entry point
```

See [docs/refactoring.md](docs/refactoring.md) for architecture details.

## Documentation

- [Installation Guide](docs/installation.md) - Detailed setup instructions
- [Refactoring Guide](docs/refactoring.md) - Architecture and code organization
- [CLAUDE.md](CLAUDE.md) - Developer reference for AI assistants

## Troubleshooting

**Camera not found:**
- Check camera permissions in system settings
- Try different camera indices in dropdown

**Slow performance:**
- Ensure GPU acceleration is enabled (check console output)
- Try switching to face tracking mode (lighter processing)

**Import errors:**
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

For more help, see [docs/installation.md](docs/installation.md#troubleshooting).

## About

Developed for Drane Engineering's assistive robotic arm project.

**Website**: [draneengineering.com](https://www.draneengineering.com/)

## License

See [LICENSE.txt](LICENSE.txt) for details.
