#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import tf

br = tf.TransformBroadcaster();
def get_param(name, value=None):
    private = "~%s" % name
    if rospy.has_param(private):
        return rospy.get_param(private)
    elif rospy.has_param(name):
        return rospy.get_param(name)
    else:
        return value

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('updateArm', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = JointState()
    msg.name = ['joint1', 'joint2','joint3', 'joint4'];
    msg.position = [0,0,0,0,0,0]
    
    source_list = get_param("source_list", [])
    rospy.loginfo(str(source_list))
    while not rospy.is_shutdown():
        msg.header.stamp = rospy.Time.now();
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass