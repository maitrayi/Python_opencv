# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:37:42 2018

@author: hp
"""

import cv2 
def main():
    path="C:\\Users\\sonau\\OneDrive\\open cv\\misc\\4.1.08.tiff"
    img = cv2.imread(path)
    #pixel = img[40:10]
    #print(pixel)  
   # print(img)
    cv2.imshow('lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
