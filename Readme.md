# YOLO Project

A project implementing the YOLO (You Only Look Once) object detection algorithm.

## Features

- Real-time object detection
- High accuracy and speed
- Easy to use and customize

## Prerequisites

- Python 3.x installed on your system

## Installation & Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/Yolo.git
    cd Yolo
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv yolo8env
    source yolo8env/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    > **Note:**  
    > The `requirements.txt` includes:
    > - `cvzone==1.6.1`
    > - `ultralytics==8.3.144`
    > - `cv2` (Install via `opencv-python` if you encounter issues)

## Usage

```bash
python detect.py --image path/to/image.jpg
```

## Project Structure

- `detect.py` - Main detection script
- `models/` - Pretrained YOLO models
- `data/` - Sample images and datasets

## Additional Notes

- If you get errors related to `cv2`, install it using:
  ```bash
  pip install opencv-python
  ```
- Activate your environment each time before running scripts:
  ```bash
  source yolo8env/bin/activate
  ```

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
