import cv2
import numpy as np

def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # # Apply adaptive thresholding to enhance text regions
    # threshold = cv2.adaptiveThreshold(blur,
    #                                   255,
    #                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                   cv2.THRESH_BINARY,
    #                                   11,
    #                                   2)
    
    # return threshold
    kernel = np.array([        
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])

    sharpen = cv2.filter2D(gray, -1, kernel)

    return sharpen


 