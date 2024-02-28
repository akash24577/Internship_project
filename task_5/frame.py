import os
from ultralytics import YOLO
import cv2


VIDEOS_DIR = os.path.join('.', 'cropped_video')


video_path = os.path.join(VIDEOS_DIR, 'test1.mp4')
video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'models', 'best.pt')

model = YOLO(model_path)

threshold = 0.5

tire_class_id = 0 # Replace with your specific tire class ID

while ret:

    results = model(frame)[0]

    tire_found = False  # Flag to track if a tire is detected
    tire_bbox = None    # Store bounding box coordinates of the detected tire

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            if int(class_id) == tire_class_id:  # Check if it's the tire class
                tire_found = True
                tire_bbox = (int(x1), int(y1), int(x2), int(y2))

                # Display bounding box on original video (optional)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

                break  # Stop iterating after finding the first tire

    if tire_found:
        x1, y1, x2, y2 = tire_bbox

        # Extract the tire region from the frame
        tire_roi = frame[y1:y2, x1:x2]

        # Create a new window for displaying the tire
        cv2.namedWindow("Tire", cv2.WINDOW_NORMAL)
        cv2.imshow("Tire", tire_roi)

        # Handle keyboard input (optional)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # Write the original video frame to the output file
    out.write(frame)

    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()