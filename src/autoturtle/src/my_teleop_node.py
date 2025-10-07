#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import curses

def main(stdscr):
    rospy.init_node('my_teleop_node')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    try:
        while not rospy.is_shutdown():
            key = stdscr.getch()
            twist = Twist()

            if key == ord('w'):
                rospy.loginfo("Moving forward")
                twist.linear.x = 1.0
            elif key == ord('s'):
                rospy.loginfo("Moving backward")
                twist.linear.x = -1.0
            elif key == ord('a'):
                rospy.loginfo("Turning left")
                twist.angular.z = 1.0
            elif key == ord('d'):
                rospy.loginfo("Turning right")
                twist.angular.z = -1.0
            elif key == ord('q'):
                break
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            pub.publish(twist)
            rospy.sleep(0.1)
    finally:
        curses.endwin()

if __name__ == '__main__':
    curses.wrapper(main)
