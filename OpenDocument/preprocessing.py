# -*- coding: utf-8 -*-
"""
@author: sabari
"""

import cv2
from skimage.filters import threshold_sauvola
import numpy as np

def sauvola_thresholding(grayImage_, window_size=15):
    """
    Sauvola thresholds are local thresholding techniques that are 
    useful for images where the background is not uniform, especially for text recognition.
    
    grayImage_ --- Input image should be in 2-Dimension Gray Scale format.
    window_size --- It represents the filter window size.
    """
    # Assert the input conditions
    assert len(grayImage_.shape) == 2, "Input image must be a 2-dimensional gray scale image."
    assert isinstance(window_size, int) and window_size > 0, "Window size must be a positive integer."
    
    thresh_sauvolavalue = threshold_sauvola(grayImage_, window_size=window_size)
    thresholdImage_ = (grayImage_ > thresh_sauvolavalue)
    
    return thresholdImage_

def remove_Lines(binaryImage_, horz_size=12, vert_size=15):
    """
    Removing the horizontal and vertical lines in the image.
    
    binaryImage_ --- Image should be in binary format.
    horz_size -- It represents the Minimum size of horizontal line need to be removed from the image.
    vert_size -- It represents the Minimum size of vertical line need to be removed from the image.
    """
    # Assert the input conditions
    assert len(binaryImage_.shape) == 2, "Input image must be a 2-dimensional binary image."
    assert binaryImage_.dtype == np.uint8, "Input image must be in binary format (np.uint8)."
    assert isinstance(horz_size, int) and horz_size > 0, "Horizontal size must be a positive integer."
    assert isinstance(vert_size, int) and vert_size > 0, "Vertical size must be a positive integer."
    
    horz_size = round(binaryImage_.shape[0] * 0.075)
    vert_size = round(binaryImage_.shape[1] * 0.09)
    
    horizontal_kernel = np.ones((1, horz_size), np.uint8)
    vertical_kernel = np.ones((vert_size, 1), np.uint8)
    
    hz_closing = cv2.morphologyEx(binaryImage_, cv2.MORPH_CLOSE, horizontal_kernel)
    ver_closing = cv2.morphologyEx(binaryImage_, cv2.MORPH_CLOSE, vertical_kernel)

    Lines = hz_closing & ver_closing
    LinesRemoved = binaryImage_ | (~Lines)
    
    return np.uint8(LinesRemoved)

    
    
        
"""
thresholdImage=preprocessing.sauvola_thresholding(grayImage)

removeLines=preprocessing.remove_Lines(np.uint8(thresholdImage))

"""

    ## remove lines ###


