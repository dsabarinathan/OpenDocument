# -*- coding: utf-8 -*-
"""
@author: sabari
"""

import cv2
from skimage.filters import threshold_sauvola
import numpy as np


class preprocessing():

    def sauvola_thresholding(grayImage_,window_size=15):
        
        """"
        Sauvola thresholds are local thresholding techniques that are 
        useful for images where the background is not uniform, especially for text recognition
        
        grayImage--- Input image should be in 2-Dimension Gray Scale format
        window_size --- It represents the filter window size 
        
        """
        thresh_sauvolavalue = threshold_sauvola(grayImage_, window_size=window_size)
    
        thresholdImage_=(grayImage_>thresh_sauvolavalue)
        
        return thresholdImage_
    
    
    def remove_Lines(binaryImage_,horz_size=12,vert_size=15):
        """
        Removing the horizontal and vertical lines in the image
        
        binaryImage_--- Image should be in binray format
        horz_size --   It represents the Minimum size of horizantal line need to be removed from the image
        vert_size --   It represents the Minimum size of vertical line need to be removed from the image
        
        """
        horz_size=round(binaryImage_.shape[0]*0.075)
        vert_size=round(binaryImage_.shape[1]*0.09)
        horizontal_kernel=np.ones((1,horz_size),np.uint8)
        vertical_kernel=np.ones((vert_size,1),np.uint8)
        hz_closing = cv2.morphologyEx(binaryImage_, cv2.MORPH_CLOSE, horizontal_kernel)
        ver_closing = cv2.morphologyEx(binaryImage_, cv2.MORPH_CLOSE, vertical_kernel)

        Lines = hz_closing&ver_closing
        LinesRemoved= binaryImage_| (~Lines)
        return np.uint8(LinesRemoved)

        
    
    
        
"""
thresholdImage=preprocessing.sauvola_thresholding(grayImage)

removeLines=preprocessing.remove_Lines(np.uint8(thresholdImage))

"""

    ## remove lines ###


