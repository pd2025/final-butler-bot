import motoron
import time
import RPi.GPIO as GPIO

mc1 = motoron.MotoronI2C(address=0x10)  # Assuming address 0x20 for the first Motoron board
mc2 = motoron.MotoronI2C()  # Assuming address 0x21 for the second Motoron board

mc1.reinitialize()
mc2.reinitialize()
mc1.disable_crc()
mc2.disable_crc()
MOVE_PIN = 23
DIR_PIN = 24

# GPIO.setmode(GPIO.BCM)  # Set GPIO numbering scheme to BCM
# GPIO.setup(MOVE_PIN, GPIO.OUT)  # Set GPIO_PIN as an output pin
# GPIO.setup(DIR_PIN, GPIO.OUT)

mc1.clear_reset_flag()
mc2.clear_reset_flag()

# config motor 1 - front right (mc1)
mc1.set_max_acceleration(1,  140)
mc1.set_max_deceleration(1, 300)

# config motor 2 - front left (mc1)
mc1.set_max_acceleration(2,  140)
mc1.set_max_deceleration(2, 300)

# config motor 3 - back right (mc2)
mc2.set_max_acceleration(3,  140)
mc2.set_max_deceleration(3, 300)

# def ardMotor(speed):
#     GPIO.output(MOVE_PIN, GPIO.HIGH)

#     if speed > 0: 
#         GPIO.output(DIR_PIN, GPIO.HIGH)
#     elif speed < 0: 
#         GPIO.output(DIR_PIN, GPIO.LOW)

# def ardMotorStop():
#     GPIO.output(MOVE_PIN, GPIO.LOW)

def stop_all_motors():
    mc1.set_speed(1, 0)
    mc1.set_speed(2, 0)
    mc2.set_speed(3, 0)
    # ardMotorStop()

def move_forward(speed):
    mc1.set_speed(1, speed)
    mc1.set_speed(2, speed)
    mc2.set_speed(3, speed)
    # ardMotor(speed)

def move_reverse(speed):
    mc1.set_speed(1, -1 * speed)
    mc1.set_speed(2, -1 * speed)
    mc2.set_speed(3, -1 * speed)
    # ardMotor(-1 * speed)

def translate_right(speed):
    mc1.set_speed(1, -1 * speed)
    mc1.set_speed(2, speed)
    mc2.set_speed(3, speed)
    # ardMotor(-1 * speed)

def translate_left(speed):
    mc1.set_speed(1, speed)
    mc1.set_speed(2, -1 * speed)
    mc2.set_speed(3, -1 * speed)
    # ardMotor(speed)

def turn_right(speed):
    mc1.set_speed(1, speed)
    mc1.set_speed(2, speed)
    mc2.set_speed(3, speed)
    # ardMotor(speed)
    
def turn_left(speed):
    mc1.set_speed(1, -1 * speed)
    mc1.set_speed(2, -1 * speed)
    mc2.set_speed(3, -1 * speed)
    # ardMotor(-1 * speed)


try:
    move_forward(800)
    move_reverse(800)
    translate_right(800)
    translate_left(800)

except KeyboardInterrupt:
    pass