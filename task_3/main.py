import cv2
import numpy as np

# img=cv2.imread("D:/Intern/task_3/road.jpg")

# converting to grayscale :
# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("window",img_gray)
# cv2.waitKey(0)

#RGB 
# img[:,:,1]=0
# cv2.imshow("window",img)
# cv2.waitKey(0)

#resizeee
# img_resize=cv2.resize(img,(256,256))
# cv2.imshow("window",img_resize)
# cv2.waitKey(0)

#flipping
# img_flip=cv2.flip(img,-1)
# cv2.imshow("window",img_flip)
# cv2.waitKey(0)

#cropping
# img_crop=img[0:300,0:300]
# cv2.imshow("window",img_crop)
# cv2.waitKey(0)


#drawing shapes
# img=np.zeros((512,512,3))

#rectangle 
# cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)

# cv2.circle(img,centre=(100,400),radius=50,color=(0,0,255),thickness=3)

 
#events  for MOUSE BUTTONS WITH BLACK IMAGE

# import cv2
# import numpy as np

# # Function to handle mouse events
# def mouse_event(event, x, y, flags, param):
#     global img
#     if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
#         cv2.circle(img, (x, y), 50, (0, 255, 0), -1)  # Draw a green circle
#     elif event == cv2.EVENT_RBUTTONDOWN:  # Right mouse button clicked
#         cv2.rectangle(img, (x - 50, y - 50), (x + 50, y + 50), (0, 0, 255), -1)  # Draw a red rectangle
#     cv2.imshow('Image', img)

# # Create a black image window
# img = np.zeros((512, 512, 3), np.uint8)

# # Display the image
# cv2.imshow('Image', img)

# # Set the mouse callback function
# cv2.setMouseCallback('Image', mouse_event)

# while True:
#     # Wait for a key event and check if it is the 'q' key to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Close all OpenCV windows
# cv2.destroyAllWindows()





#cropping tool
# import cv2

# # Global variables to track mouse events
# drawing = False
# ix, iy = -1, -1
# cropped_img = None

# # Mouse callback function
# def draw_rectangle(event, x, y, flags, param):
#     global ix, iy, drawing, cropped_img

#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y

#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             img_copy = img.copy()
#             cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
#             cv2.imshow('Image', img_copy)

#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
#         cv2.imshow('Image', img)
#         cropped_img = img[iy:y, ix:x]
#         cv2.imshow('Cropped Image', cropped_img)

# # Load image
# img = cv2.imread("D:/Intern/task_3/road.jpg")

# # Create a window and set mouse callback
# cv2.imshow('Image', img)
# cv2.setMouseCallback('Image', draw_rectangle)

# while True:
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break

# cv2.destroyAllWindows()




#WORKING WITH VIDEOS
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("webcam",frame)

    if cv2.waitkey(1) & 0xFF == ord('x'):
        break
    # cv2.destroyAllWindows
    cv2.waitKey(0)