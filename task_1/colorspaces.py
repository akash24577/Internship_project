
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Project\img\image.jpg')
cv.imshow(' Flower', img)

# plt.imshow(img)
# plt.show()
# Define a maximum display size
max_display_size = (800, 600)

# Resize the image if it exceeds the maximum display size
height, width = img.shape[:2]
if height > max_display_size[1] or width > max_display_size[0]:
    img = cv.resize(img, max_display_size, interpolation=cv.INTER_AREA)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)