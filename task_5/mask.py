import os
from ultralytics import YOLO
import numpy as np
import cv2


VIDEOS_DIR = os.path.join('.', 'videos')

video_path = os.path.join(VIDEOS_DIR, 'test1.mp4')
video_path_out = '{}_crop_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'models', 'best.pt')
model = YOLO(model_path) 

threshold = 0.5

while ret:

    results = model(frame)[0]

    mask = np.zeros((H, W, 3), dtype=np.uint8)  

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            if int(class_id) == 0: 
                cv2.rectangle(mask, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), thickness=-1)

    masked_frame = cv2.bitwise_and(frame, mask)

    out.write(masked_frame)

    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()
