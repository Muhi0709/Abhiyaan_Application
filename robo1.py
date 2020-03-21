#This method assumes roscore,turtlesim is made running using the Terminal commands
#Also,it is assumed Abhiyaan is spawned at the given location using the rosservice call command
#The node is executed once turtle1 and abhiyaan are spawned
#First rotation(1sec) and then straightline motion towards goal(1sec)

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
    global orient
    #flag variable is to ensure x,y,orient holds only the initial value
    global flag
    if(flag==0):
        x=current_pos.x                
        y=current_pos.y                
        orient=current_pos.theta
        flag+=1

#obtaining position of turtle1 using a subscriber node
def position():
    rospy.Subscriber("/turtle1/pose",Pose,getpose)                   


def getgoalpose(cur_pos):
    global x0
    global y0
    x0=cur_pos.x
    y0=cur_pos.y

#obtaining position of abhiyaan using a subscriber node
def goalposition():
    rospy.Subscriber("/abhiyaan/pose",Pose,getgoalpose)            
    print "Finding the Location of Abhiyaan"                       

#publisher node to publish the angular velocity to turtle1
#turtle1 rotates to face  Abhiyaan
def rotate():
    global x
    global y
    global x0
    global y0
    global orient
    message=Twist()                                                 
    t2=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)       
    fi_angle=math.atan2(y0-y,x0-x)
    print "Rotating by %f radians " %(fi_angle-orient)
    message.angular.z=(fi_angle-orient)                             
    time.sleep(1)
    t2.publish(message)

#publisher node to publish the linear velocity to turtle1
#turtle1 moves in a straight line and stops 2 units before Abhiyaan
def linear():
    global x
    global y
    global x0
    global y0
    message=Twist()
    t3=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)      
    distance=abs(math.sqrt((x-x0)**2+(y-y0)**2))
    message.linear.x=(distance-2.0)
    print "Moving by %f units" %message.linear.x                    
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
        
