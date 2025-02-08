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



![image](https://github.com/user-attachments/assets/1b090cf3-779a-4d80-87b0-c093eafcabb0)



