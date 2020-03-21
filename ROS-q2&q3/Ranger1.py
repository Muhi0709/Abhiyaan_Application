
import rospy
from std_msgs.msg import String

#message is published at a rate of 0.5Hz    
def talk():
    p = rospy.Publisher('welcome_message', String, queue_size=10)
    rospy.init_node('Ranger1', anonymous=True)
    rate=rospy.Rate(0.5)                   
    while not rospy.is_shutdown():
        #message is publised over the topic
        #no printing of message in the terminal or to the node's logfile(loginfo())
        stri = "Welcome to Abhiyaan"    
        p.publish(stri)                 
        rate.sleep()                    

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass



