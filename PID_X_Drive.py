import numpy as np
import cv2
import Encoder
import time
import motoron
import math

enc = Encoder.Encoder(24, 10)
mc.motoron.Motoron12C()

# # configure motor 1
# mc.set_max_acceleration(1, 140)
# mc.set_max_deceleration(1, 300)

# # configure motor 2
# mc.set_max_acceleration(2, 140)
# mc.set_max_deceleration(2, 300)

# # configure motor 3
# mc.set_max_acceleration(3, 140)
# mc.set_max_deceleration(3, 300)

# # configure motor 4
# mc.set_max_acceleration(4, 140)
# mc.set_max_deceleration(4, 300)

mc.reinitialize()
mc.disable_crc()

enc.read()
kp = 0
ki = 0
kd = 0
error = 0
totalError = 0
lastError = 0
target = 0
pid = (kp * error) + (ki * totalError) + (kd * (error - lastError))
# the numbers 24, 10 represent the pin numbers that it will be attached to in the raspberry pi
enc_1 = Encoder.Encoder(24, 10)
enc_2 = Encoder.Encoder(25, 9)
enc_1.read()
enc_2.read()
print(enc_1.read())


class PID_X_Drive():

    def __init__(self):
        self.mc1_max_acceleration = mc.set_max_acceleration(1, 140)
        self.mc1_max_deceleration = mc.set_max_deceleration(1, 300)
        self.mc2_max_acceleration = mc.set_max_acceleration(2, 140)
        self.mc2_max_deceleration = mc.set_max_deceleration(2, 300)
        self.mc3_max_acceleration = mc.set_max_acceleration(3, 140)
        self.mc3_max_deceleration = mc.set_max_deceleration(3, 300)
        self.mc4_max_acceleration = mc.set_max_acceleration(4, 140)
        self.mc4_max_deceleration = mc.set_max_deceleration(4, 300)
        self.reinitialize = mc.reinitialize()
        self.disable_crc = mc.disable_crc()

    def PID_X_Drive_y_axis(target):
        try:
            while True:
                enc_1_value = enc_1.read()
                enc_2_value = enc_2.read()
                error = ultrasonic_reading
                derivative = error - lastError
                pid = (kp * error) + (kd * derivative)
                
                # change these values because not all motor can be running in the same direction at once
                mc.set_speed(1, pid)
                mc.set_speed(2, pid)
                mc.set_speed(3, pid)
                mc.set_speed(4, pid)

                error = lastError
                time.sleep(0.05)
                if error == 0:
                    break
            # stop motors
        except KeyboardInterrupt:
            pass

    def PID_X_Drive_x_axis(target):
        try:
            while True:
                enc_1_value = enc_1.read()
                enc_2_value = enc_2.read()
                error = ultrasonic_reading
                derivative = error - lastError
                pid = (kp * error) + (kd * derivative)
                
                # change these values because not all motor can be running in the same direction at once
                mc.set_speed(1, pid)
                mc.set_speed(2, pid)
                mc.set_speed(3, pid)
                mc.set_speed(4, pid)

                error = lastError
                time.sleep(0.05)
                if error == 0:
                    break
            # stop motors
        except KeyboardInterrupt:
            pass

    def Basic_X_Drive_forward():
        # front right motor spin forward
        # front left motor spin reverse
        # back right motor spin reverse
        # back left motor spin forward

PID_X_Drive(500)