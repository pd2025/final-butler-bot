# arm_control.py
import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600)

def move_arm(position):
    arduino.write(position.encode())
    time.sleep(1)

def grab_object():
    move_arm('GRAB')

def release_object():
    move_arm('RELEASE')
