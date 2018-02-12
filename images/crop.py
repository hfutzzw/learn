import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg', 1)
cv2.imshow('Image_before_crop',img)
img_crop = img[100:200,100:200]
cv2.imshow('Image_after_crop',img_crop)

cv2.waitKey(0)

cv2.destroyAllWindows()

