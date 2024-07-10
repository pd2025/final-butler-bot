import motoron
import time
import RPi.GPIO as GPIO

class basic_X_drive:

    def __init__(self):
        self.mc1 = motoron.MotoronI2C(address=0x20)  # Assuming address 0x20 for the first Motoron board
        self.mc2 = motoron.MotoronI2C(address=0x21)  # Assuming address 0x21 for the second Motoron board
        self.configure_motors()
        self.mc1.reinitialize()
        self.mc2.reinitialize()
        self.mc1.disable_crc()
        self.mc2.disable_crc()
        self.MOVE_PIN = 23
        self.DIR_PIN = 24
        GPIO.setmode(GPIO.BCM)  # Set GPIO numbering scheme to BCM
        GPIO.setup(self.MOVE_PIN, GPIO.OUT)  # Set GPIO_PIN as an output pin
        GPIO.setup(self.DIR_PIN, GPIO.OUT)

    def configure_motors(self):
        # config motor 1 - front right (mc1)
        self.mc1.set_max_acceleration(1,  140)
        self.mc1.set_max_deceleration(1, 300)

        # config motor 2 - front left (mc1)
        self.mc1.set_max_acceleration(2,  140)
        self.mc1.set_max_deceleration(2, 300)

        # config motor 3 - back right (mc2)
        self.mc2.set_max_acceleration(1,  140)
        self.mc2.set_max_deceleration(1, 300)

    def ardMotor(self, speed):
        GPIO.output(self.MOVE_PIN, GPIO.HIGH)

        if speed > 0: 
            GPIO.output(self.DIR_PIN, GPIO.HIGH)
        elif speed < 0: 
            GPIO.output(self.DIR_PIN, GPIO.LOW)

    def ardMotorStop(self):
        GPIO.output(self.MOVE_PIN, GPIO.LOW)

    def stop_all_motors(self):
        self.mc1.set_speed(1, 0)
        self.mc1.set_speed(2, 0)
        self.mc2.set_speed(1, 0)
        self.ardMotorStop(self)

    def move_forward(self, speed):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, speed)
        self.ardMotor(speed)

    def move_reverse(self, speed):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, -1 * speed)
        self.ardMotor(-1 * speed)

    def translate_right(self, speed):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, speed)
        self.ardMotor(-1 * speed)

    def translate_left(self, speed):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, -1 * speed)
        self.ardMotor(speed)

    def turn_right(self, speed):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, speed)
        self.ardMotor(speed)
        
    def turn_left(self, speed):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, -1 * speed)
        self.ardMotor(-1 * speed)

drivetrain = basic_X_drive()

try:
    drivetrain.move_forward(800)
    drivetrain.move_reverse(800)
    drivetrain.translate_right(800)
    drivetrain.translate_left(800)

except KeyboardInterrupt:
    pass
finally:
    drivetrain.stop_all_motors()