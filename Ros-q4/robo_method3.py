#This method assumes roscore,turtlesim is made running using the Terminal commands
#Also,it is assumed Abhiyaan is spawned at the given location using the rosservice call command
#The node is executed once turtle1 and abhiyaan are spawned
#Smooth motion involving both linear and angular motion simultaneously(proportional controller) 
#changing proportionality constants changes the path


import rospy
import time
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#position of turtle1(value changes throughout the motion)
x=0.0
y=0.0                    
orient=0.0

#position of abhiyaan
x0=0.0
y0=0.0 
                 
def getpose(current_pos):
    global x
    global y
    global orient
    x=current_pos.x
    y=current_pos.y
    orient=current_pos.theta

#subscriber node for the position of turtle1

def position():	
    rospy.Subscriber("/turtle1/pose",Pose,getpose)                   
	
	
def getgoalpose(cur_pos):
    global x0
    global y0
    x0=cur_pos.x
    y0=cur_pos.y

#subscriber node for the position of abhiyaan

def goalposition():
    rospy.Subscriber("/abhiyaan/pose",Pose,getgoalpose)               
    print "Finding the Location of Abhiyaan"


#publisher node to publish both linear and angular velocity
def move():
    global x
    global y
    global x0
    global y0
    global orient
    message=Twist()
    bot=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10) 

    #proportionality constants        
    K1=0.5
    K2=0.75 
                                                            
    print "Moving towards Abhiyaan...\n Coordinates:"
    while(True):
        angle=math.atan2(y0-y,x0-x)
        dist=abs(math.sqrt((x-x0)**2+(y-y0)**2))

        #linear speed is proportinal to distance btw the turtles
        #angular speed is proportional to angle btw the turtles
        linear_speed=dist*K1                                      
        angular_speed=(angle-orient)*K2                            

        message.linear.x=linear_speed
        message.angular.z=angular_speed
		
        bot.publish(message)
        print "x=",x,"y=",y,"Distance: ",dist,"Angle btw turtles: ",(angle-orient)
        if(dist<=2):
            print "Abhiyaan found!!!!!"
            break
	
	

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
        move()
        print "Final location of turtle1:\n x: %f \ny: %f \norientation: %f" %(x,y,orient)
    except rospy.ROSInterruptException:
        pass
