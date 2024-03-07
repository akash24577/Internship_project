import os
from ultralytics import YOLO
import cv2
import math

VIDEOS_DIR = os.path.join('.', 'cropped_video')
video_path = os.path.join(VIDEOS_DIR, 'test_2.mp4')

cap = cv2.VideoCapture(video_path)

model_path = os.path.join('.', 'models', 'best.pt')
model = YOLO(model_path)
threshold = 0.5

common_point_1 = None  # Initialize the first common point
common_point_2 = (300, 300)  # Initialize the second common point (replace with desired values)

# Radius of the tire in meters
tire_radius = 0.3  # Assuming the tire radius is 0.3 meters

# Speed of rotation in km/hr
rotation_speed_km_hr = 1.2

# Convert rotation speed to radians per second
rotation_speed_rad_sec = (rotation_speed_km_hr * 1000) / (3600 * tire_radius)

# Time elapsed between frames (in seconds)
frame_rate = cap.get(cv2.CAP_PROP_FPS)
time_elapsed_per_frame = 1 / frame_rate

# Initialize angle of rotation
angle_rad = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Assign the first detected point as the first common point
            if common_point_1 is None:
                common_point_1 = (center_x, center_y)

            # Rotate the second point around the first common point
            rotate_angle_deg = math.degrees(angle_rad)
            rotate_distance = 140  # Adjust the distance between the common point and the rotating point
            point2_x = int(common_point_1[0] + rotate_distance * math.cos(math.radians(rotate_angle_deg)))
            point2_y = int(common_point_1[1] + rotate_distance * math.sin(math.radians(rotate_angle_deg)))

            # Draw center point, first common point, second common point, and rotating point
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # Center point
            cv2.circle(frame, common_point_1, 5, (255, 0, 0), -1)  # First common point
            cv2.circle(frame, common_point_2, 5, (255, 0, 0), -1)  # Second common point
            cv2.circle(frame, (point2_x, point2_y), 5, (255, 0, 0), -1)  # Rotating point

            # Draw lines between common points, center point, and rotating point
            cv2.line(frame, common_point_1, (point2_x, point2_y), (255, 0, 0), 2)  # Line to rotating point
            # cv2.line(frame, common_point_2, (point2_x, point2_y), (0, 255, 0), 2)  # Line to rotating point
            cv2.line(frame, common_point_1, (center_x, center_y), (0, 0, 255), 2)  # Line to center point
            cv2.line(frame, common_point_2, (center_x, center_y), (0, 255, 0), 2)  # Line to rotating point

            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            cv2.putText(frame, f"Angle: {rotate_angle_deg:.2f} degrees", (int(x1), int(y2 + 30)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Object Detection', frame)

    # Predict the angle of rotation
    angle_rad += rotation_speed_rad_sec * time_elapsed_per_frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()