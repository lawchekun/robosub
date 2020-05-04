#!/usr/bin/env python

import threading
import getch # Needs apt install python-pip & pip install https://pypi.python.org/packages/source/g/getch/getch-1.0-python2.tar.gz#md5=586ea0f1f16aa094ff6a30736ba03c50
import rospy

class KeyboardThread(threading.Thread):
    # Credits to https://stackoverflow.com/a/57387909/5901346
    def __init__(self, input_cbk = None, name='keyboard_input_thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        rospy.loginfo('KeyboardThread: ready')
        rate = rospy.Rate(50)
        while not rospy.is_shutdown():
            self.input_cbk(getch.getch()) # Waits to get input then gives it to the callback
            rate.sleep()

if __name__ == "__main__":
    def keyboard_callback(ch):
        rospy.loginfo('You Entered:{}'.format(ch))
        # TODO: Publish stuff to the thrusters

    rospy.init_node('keyboard_input_thread')
    try:
        node = KeyboardThread(keyboard_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        print('KeyboardThread::Exception')
    print('Leaving KeyboardThread')
