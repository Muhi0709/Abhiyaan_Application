import cv2 as cv
import numpy as np

def signal_detector():
    #making a list of images
    image=[cv.imread("1.png"),cv.imread("2.png"),cv.imread("3.png")]
    #all 3 images are of same size
    s1,s2,s3=np.shape(image[0])
    for k in [0,1,2]:
        red=0
        yellow=0
        green=0    
        for i in range(s1):
            for j in range(s2):
                #bgr format and assuming all colors in the image are perfect red green and yellow(255 pixel value)
                if(image[k][i][j][0]==0 and image[k][i][j][1]==0 and image[k][i][j][2]==255):
                    red+=1
                    break
                elif(image[k][i][j][0]==0 and image[k][i][j][1]==255 and image[k][i][j][2]==0):
                    green+=1
                    break
                elif(image[k][i][j][0]==0 and image[k][i][j][1]==255 and image[k][i][j][2]==255):
                    yellow+=1
                    break
            #checking for the pixel value -channelwise(BGR)
            if(red!=0 or green!=0 or yellow!=0):
                break
        if(red!=0):
            print "Image ",k+1,": RED"
        elif(green!=0):
            print "Image ",k+1,": GREEN"
        elif(yellow!=0):
            print "Image ",k+1,": YELLOW"

if __name__=='__main__':
    try:
        signal_detector()
    except:
        pass


