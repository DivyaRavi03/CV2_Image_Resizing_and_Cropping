# Image Resizing and Cropping
This is an another fundamental image preprocessing techniques using python and OpenCV. The script loads an image, resized it to specific dimensions mentioned and crops a defined region of interest(ROI - specific part of image rather than whole).

# Technologies used
- Ubuntu
- Python
- OpenCV
- Numpy

# What it does
- Loads an image from a file.
- Resizes the image to a predefined width and height using 'cv2.resize()' function.
- Crops a ROI (specific part of an image) from original using Numpy array slicing.
- Displays original, resized, and cropped images separately.

 # Steps to follow
 - Run the py file with image or image_path changed.

# Key concepts:
- **Image Resizing** - This allows to create uniform input sizes to feed machine learning models.
- **Cropping using Numpy slicing** - This is possible because images are changed to arrays (each pixels to matrix) using Numpy so that it can be manipulated directly and efficiently.
