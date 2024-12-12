from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.yaml")

results = model.train(data="C:\\Users\\anike\\OneDrive\\Desktop\\AUTOMATIC-AMBULANCE-DETECTION-SYSTEM-FOR-EMERGENCY-VEHICLE\\data.yaml", epochs=30)
