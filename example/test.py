# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:27:27 2024

@author: SABARI
"""
import cv2

import numpy as np

from OpenDocument.preprocessing import remove_lines, sauvola_thresholding

from matplotlib import pyplot as plt

image = cv2.imread("back_ground.jpg")


gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

### document image adaptive binarization 


binary_image = sauvola_thresholding(gray_image,window_size=15)

# Plot the original and binary images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Binary Image')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

plt.show()

### document image line removal 

image1 =  cv2.imread("lines.png")


gray_image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

### document image adaptive binarization 


binary_image1 = sauvola_thresholding(gray_image1,window_size=15)


line_removed = remove_lines(np.uint8(binary_image1),horz_size =15,vert_size=15)
# Plot the original and line removed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(gray_image1, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Lines Removed Image')
plt.imshow(line_removed, cmap='gray')
plt.axis('off')

plt.show()
