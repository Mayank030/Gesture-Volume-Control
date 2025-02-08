# Gesture Volume Control

## 🎛 Gesture Volume Control

Control your system volume using hand gestures with OpenCV & MediaPipe!

### 📌 Overview

This project enables users to control their computer’s audio volume using hand gestures. By leveraging Python, OpenCV, MediaPipe, and Pycaw, it tracks hand movements in real-time and adjusts the system volume accordingly.


### 📌 Project Structure

HandTrackingModule.py: Contains the handDetector class with findHands() and findPosition() functions for hand tracking.

VolumeHandControl.py: Imports HandTrackingModule.py and uses its functionalities to control the system volume based on hand gestures.


### 🔧 Features

✅ Real-time hand tracking using MediaPipe Hands

✅ Adjust system volume based on hand gestures

✅ Intuitive and contactless volume control

✅ Uses OpenCV for video processing

✅ Pycaw to control system volume


### 🛠 Tech Stack

Python

OpenCV (for video processing)

MediaPipe (for hand tracking)

Pycaw (for volume control automation)

Numpy (for numerical operations)


### 🚀 How It Works

The webcam captures hand movements.

MediaPipe detects hand landmarks.

The distance between the thumb and index finger determines the volume level.

Pycaw adjusts the system volume accordingly.


### Hand Landmarks

![image](https://github.com/user-attachments/assets/1b090cf3-779a-4d80-87b0-c093eafcabb0)


### Mediapipe

STATIC_IMAGE_MODE:

If set to false, the solution treats the input images as a video stream. It will try to detect hands in the first input images, and upon a successful detection further localizes the hand landmarks. In subsequent images, once all max_num_hands hands are detected and the corresponding hand landmarks are localized, it simply tracks those landmarks without invoking another detection until it loses track of any of the hands. This reduces latency and is ideal for processing video frames. If set to true, hand detection runs on every input image, ideal for processing a batch of static, possibly unrelated, images. Default to false.

MAX_NUM_HANDS:

Maximum number of hands to detect. Default to 2.

MODEL_COMPLEXITY:

Complexity of the hand landmark model: 0 or 1. Landmark accuracy as well as inference latency generally go up with the model complexity. Default to 1.

MIN_DETECTION_CONFIDENCE:

Minimum confidence value ([0.0, 1.0]) from the hand detection model for the detection to be considered successful. Default to 0.5.

MIN_TRACKING_CONFIDENCE:

Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the hand landmarks to be considered tracked successfully, or otherwise hand detection will be invoked automatically on the next input image. Setting it to a higher value can increase robustness of the solution, at the expense of a higher latency. Ignored if static_image_mode is true, where hand detection simply runs on every image. Default to 0.5.

Source : https://mediapipe.readthedocs.io/en/latest/solutions/hands.html
