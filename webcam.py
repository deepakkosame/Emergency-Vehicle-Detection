import cv2

from ultralytics import YOLO


model_path = r"C:\\Users\\anike\\OneDrive\\Desktop\\AUTOMATIC-AMBULANCE-DETECTION-SYSTEM-FOR-EMERGENCY-VEHICLE\\runs\\detect\\train\\weights\\best.pt"
model = YOLO(model_path)


threshold = 0.5


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


cv2.namedWindow('Real-Time Vehicle Detection', cv2.WINDOW_NORMAL)

while True:

    ret, frame = cap.read()


    if not ret:
        print("Error: Failed to read frame from webcam.")
        break


    results = model(frame)[0]


    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            label = f"{results.names[int(class_id)].upper()} {score * 100:.1f}%"

            cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Real-Time Vehicle Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWin5263dows()
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)
