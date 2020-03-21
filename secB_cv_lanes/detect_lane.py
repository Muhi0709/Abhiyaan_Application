import cv2 as cv
import numpy as np

def lane_detect():
    original_image=cv.imread('lanes.jpeg')    
    gray_image=cv.cvtColor(original_image,cv.COLOR_BGR2GRAY)
    #to get  the edges in the image (containing the lanes)
    canny_image=cv.Canny(gray_image,210,220)                  
    det_lines=cv.HoughLinesP(canny_image,1,np.pi/180,50,minLineLength=100,maxLineGap=10)    
    for line in det_lines:
        x1,y1,x2,y2=line[0]
        #drawing lines over the detected lanes
        cv.line(original_image,(x1,y1),(x2,y2),(0,0,255),3)   
    
    cv.imshow('detection',original_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    try:
        lane_detect()
    except:
        pass
