# -*- coding: utf-8 -*-
import time
import sys

sleep_time  = sys. argv[1]

def sleep():
    print ('Going to sleep for', sleep_time, 'seconds')
    for x in range(0, int(sleep_time)):
        time.sleep(1)
        print('.', end='', flush=True)
    print('\n')

def ftp_connect():
    print('Hello')

while True:
    ftp_connect()
    sleep()
