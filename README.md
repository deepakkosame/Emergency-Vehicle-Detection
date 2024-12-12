# Emergency-Vehicle-Detection
This repository contains an implementation of an Automatic Ambulance Detection System using YOLO (You Only Look Once) for real-time object detection. The system is designed to detect ambulances in video streams, particularly for use in scenarios such as traffic management and emergency vehicle prioritization.
The system leverages the YOLO object detection framework to identify ambulances in real time through webcam video feeds. The model is trained on a custom dataset hosted on Roboflow, and the implementation uses OpenCV for video processing.

Features
Real-time ambulance detection through a webcam feed.
Customizable detection threshold.
Lightweight and efficient YOLO-based model.

Dataset
The training dataset consists of images labeled specifically for ambulance detection. Key dataset details:
Number of Classes (nc): 1
Class Name: Ambulance
Dataset license: CC BY 4.0

Dataset is available on Roboflow:
Ambulance Dataset on Roboflow.

Installation
Clone the repository:
git clone https://github.com/your-username/automatic-ambulance-detection.git
cd automatic-ambulance-detection

Install required dependencies:
pip install -r requirements.txt
Download the YOLO model weights and place them in the specified directory.

Usage
Ensure your webcam is connected and functioning.
Run the detection script:
python webcam.py
Press q to exit the application.

Dependencies
The following Python libraries are required:
OpenCV
Ultralytics YOLO
NumPy

Install them using:
pip install opencv-python-headless ultralytics numpy

Script Details
data.yaml
Specifies the dataset paths and class information for training.

Structure:

train: ../train/images
val: ../valid/images
test: ../test/images
nc: 1
names: ['Ambulance']

webcam.py

Captures video frames from the webcam.
Uses the YOLO model to detect ambulances and overlays bounding boxes and labels on detected objects.
Detection threshold can be modified using the threshold variable.

Acknowledgements
The YOLO framework by Ultralytics for state-of-the-art object detection.
Roboflow for dataset management and hosting.
