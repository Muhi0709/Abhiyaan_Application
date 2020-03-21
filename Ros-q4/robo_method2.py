#This method assumes roscore,turtlesim is made running using the Terminal commands
#Also,it is assumed Abhiyaan is spawned at the given location using the rosservice call command
#The node is executed once turtle1 and abhiyaan are spawned
#First slow rotation and then slow straightline motion towards goal(practical method)
#slower the speeed ,greater the accuracy-tradeoff btw the two


import rospy
import time
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#position of turtle1
x=0.0
y=0.0                      
orient=0.0

#position of Abhiyaan
x0=0.0
y0=0.0 
                   
flag=0

def getpose(current_pos):
    global x
    global y
    global flag
    global orient
    
    #flag variable to make sure only initial value of x,y,orient is stored
    if(flag==0):                                 
        x=current_pos.x
        y=current_pos.y 
        orient=current_pos.theta
        flag+=1

#subscriber node for position of turtle1
def position():	
    rospy.Subscriber("/turtle1/pose",Pose,getpose)                             

	
def getgoalpose(cur_pos):
    global x0
    global y0
    x0=cur_pos.x
    y0=cur_pos.y

#subscriber node for position of Abhiyaan
def goalposition():
    rospy.Subscriber("/abhiyaan/pose",Pose,getgoalpose)                       
    print "Finding the Location of Abhiyaan"

#publisher node for rotation
#turtle1 rotates to face  Abhiyaan
def rotate():
    global x
    global y
    global x0
    global y0                                                      
    global orient
    message=Twist()
    c=0                                                           
    t2=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    fi_angle=math.atan2(y0-y,x0-x)
    print "Rotating by %f radians " %(fi_angle-orient)
    #while loop makes the difference btw this and the previous method
    while(abs((fi_angle-orient)-c)>=0.0175):
        
        #clockwise
        if((fi_angle-orient)>0):
	    #stepsize of 1 degree/sec                               
            message.angular.z=0.0175 
            #angle rotated                      
            c+=0.0175                                      
            time.sleep(1)                                  
            t2.publish(message)   

        # anticlockwise                    
        if((fi_angle-orient)<0):                  
            message.angular.z=-0.0175
            c-=0.0175
            time.sleep(1)
            t2.publish(message)
    
    #stopping the turtle1
    message.angular.z=0                             
    time.sleep(1)
    t2.publish(message)                         
		

#publisher node for linear motion
#turtle1 moves in a straight line and stops 2 units before Abhiyaan
def linear():
    global x
    global y
    global x0                                                     
    global y0
    message=Twist()
    c=0
    t3=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    distance=abs(math.sqrt((x-x0)**2+(y-y0)**2))                  
    print "Moving by %f units" %(distance-2.0)

    while(abs((distance-2.0)-c)>=0.1):
        #stepsize of 0.1 units/sec
        message.linear.x=0.1
        #distance moved
        c+=0.1                                               
        time.sleep(1)
        t3.publish(message)

    #stopping the turtle1	
    message.linear.x=0                                           
    time.sleep(1)
    t3.publish(message)
	


if __name__=="__main__":
    try:
        rospy.init_node("t1",anonymous=True)
        goalposition()
        time.sleep(1)
        print "Location of Abhiyaan:\n x: %f \n y: %f " %(x0,y0)
        position()
        time.sleep(2)
        print "Current location of turtle1(x) : %f" %x
        print "Current location of turtle1(y) : %f" %y
        print "Current location of turtle1(orientation) : %f" %orient
        rotate()
        time.sleep(2)
        linear()
    except rospy.ROSInterruptException:
        pass
