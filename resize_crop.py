import cv2
import numpy as np
img_path = "/home/divya/cv_projects/images/test_img.jpg"
img = cv2.imread(img_path)

if img is None:
	print(f"Error: Could not load image from {img_path}")
else:
	width= 300
	height = 450
	dimensions = (width, height)
	print("image is ready to resize and crop") 
	resize_img = cv2.resize(img, dimensions, interpolation = cv2.INTER_AREA)
	crop_img = img[100:500, 150:500]
	cv2.imshow("Orginial image",img)
	cv2.imshow("Resized image",resize_img)
	cv2.imshow("Cropped image", crop_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
