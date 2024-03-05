import cv2
from tracker import *

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("D:/Intern/task_8/input1.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

tracked_point = None  # Initialize a variable to store the tracked point

# import cv2
# from tracker import *

# ... (Rest of your code remains the same)

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    # Extract half of the region of interest (modify as needed)
    roi = frame[340:720, 500:700]  # Adjusted to cover half the width

    # ... (Rest of your code remains the same)


    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # 2. Object Tracking and Point Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id

        # Define the point of interest within the bounding box
        point_x = x + w // 2  # Example: Center of the bounding box
        point_y = y + h // 2  # Modify as needed based on your requirements

        # Track the point
        tracked_point = (point_x, point_y)

        # Draw bounding box and tracked point
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(roi, tracked_point, 5, (0, 0, 255), -1)  # Adjust circle size and color
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()