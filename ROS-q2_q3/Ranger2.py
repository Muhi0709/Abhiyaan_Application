import rospy
from std_msgs.msg import String

#the message/data gets printed directly
def getmsg(stri):
	print stri.data          

#subscriber gets the string message (of welcome_message topic)
#the subscription ends only when the node/program quits(press ctrl+c to quit)	    
def listen():
 	r= rospy.Subscriber('welcome_message', String,getmsg)   
	rospy.init_node('Ranger1', anonymous=True)
	rospy.spin()                    
if __name__ == '__main__':
	try:
		listen()
	except rospy.ROSInterruptException:
		pass

