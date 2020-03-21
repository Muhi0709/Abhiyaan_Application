import cv2 as cv
import numpy as np

original_image=cv.imread('lanes.jpeg')    
gray_image=cv.cvtColor(original_image,cv.COLOR_RGB2GRAY)
#to get  the edges in the image (containing the lanes)
canny_image=cv.Canny(gray_image,200,220)                  
det_lines=cv.HoughLinesP(canny_image,1,np.pi/180,50,minLineLength=100,maxLineGap=10)    
for line in det_lines:
    x1,y1,x2,y2=line[0]
    #drawing lines over the detected lanes
    cv.line(original_image,(x1,y1),(x2,y2),(0,0,255),3)   
    
cv.imshow('detection',original_image)
k=cv.waitKey(0)
cv.destroyAllWindows()
