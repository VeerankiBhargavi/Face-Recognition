# Face Detection using OpenCV

This repository contains a Python script for face detection using the OpenCV library. The script detects faces in an image and draws rectangles around them.

## Requirements

- Python 3.x
- OpenCV (cv2)

## Usage

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your_username/face-detection-opencv.git
    ```

2. Navigate to the project directory:

    ```
    cd face-detection-opencv
    ```

3. Ensure you have an input image (`img1.jpg` in this example) in the project directory.

4. Run the Python script:

    ```
    python face_detection.py
    ```

5. The script will display the input image with rectangles drawn around the detected faces.

## Explanation

- `face_detection.py`: This script contains the implementation of the face detection algorithm using OpenCV. It defines a `FaceDetector` class with methods to detect and draw faces on an image.

- `haarcascade_frontalface_default.xml`: This XML file contains the pre-trained Haar cascade classifier for face detection. It is used by OpenCV to detect faces in images.
