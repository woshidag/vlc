#!/usr/bin/env python
from vlc.srv import StartVideo
import rospy

def start():
    rospy.wait_for_service('start_video')
    try:
        start_video = rospy.ServiceProxy('start_video', StartVideo)
        resp1 = start_video('/home/jll/common/happy.mp4')
        return
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == '__main__':
    start()