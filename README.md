
🚗 Driver Fatigue Detection using Computer Vision (OpenCV)
📌 Overview

This project implements a simple real-time Driver Fatigue Detection System using computer vision techniques. The system monitors the driver through a webcam and detects prolonged eye closure to identify drowsiness. When fatigue is detected, an alert sound is triggered to warn the driver.

The goal is to demonstrate a low-cost and lightweight safety solution that can later be integrated into commercial vehicles or embedded edge devices like Raspberry Pi.

This is an early prototype developed as part of an automotive safety hackathon project.

🎯 Problem

Driver drowsiness is one of the leading causes of road accidents, especially in trucks, buses, and long-distance transport vehicles. Even a few seconds of microsleep can result in severe collisions.

Most affordable vehicles do not include advanced driver assistance systems due to high costs. Hence, there is a need for a simple and low-cost monitoring solution.

💡 Solution

This prototype uses:

Face detection

Eye detection

Eye closure time tracking

If the driver’s eyes remain closed for more than 2 seconds, the system assumes fatigue and triggers an alarm.

The entire system runs locally without internet and requires only a camera and a basic computer.

⚙️ Tech Stack

Python

OpenCV

NumPy

Haar Cascade Classifiers

(No heavy ML libraries used — lightweight and easy to deploy)

🚀 Features

✅ Real-time webcam monitoring
✅ Face and eye detection
✅ Fatigue detection based on eye closure duration
✅ Audio alert system
✅ Works offline
✅ Beginner-friendly implementation

📂 Project Structure
fatigue_opencv.py   # main detection script
README.md           # documentation

▶️ How to Run

Install dependencies:

pip install opencv-python numpy


Run:

python fatigue_opencv.py


Press ESC to exit.

🎥 Demo

Close your eyes for 2–3 seconds → the system displays DROWSY and plays an alert sound.

🔮 Future Improvements

Yawning detection

Head pose estimation

Collision detection module

Deployment on Raspberry Pi

Integration into full vehicle safety system

👥 Note

This is a prototype developed for learning and hackathon purposes. Further improvements and optimizations are planned.
