import motoron
import time

class basic_X_drive:

    def __init__(self):
        self.mc1 = motoron.MotoronI2C(address=0x20)  # Assuming address 0x20 for the first Motoron board
        self.mc2 = motoron.MotoronI2C(address=0x21)  # Assuming address 0x21 for the second Motoron board
        self.configure_motors()
        self.mc1.reinitialize()
        self.mc2.reinitialize()
        self.mc1.disable_crc()
        self.mc2.disable_crc()

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

        # config motor 4 - back left (mc2)
        self.mc2.set_max_acceleration(2,  140)
        self.mc2.set_max_deceleration(2, 300)

    def stop_all_motors(self):
        self.mc1.set_speed(1, 0)
        self.mc1.set_speed(2, 0)
        self.mc2.set_speed(1, 0)
        self.mc2.set_speed(2, 0)

    def move_forward(self, speed, time1):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, speed)
        self.mc2.set_speed(2, speed)
        time.sleep(time1)
        self.stop_all_motors()

    def move_reverse(self, speed, time1):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, -1 * speed)
        self.mc2.set_speed(2, -1 * speed)
        time.sleep(time1)
        self.stop_all_motors()

    def translate_right(self, speed, time1):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, speed)
        self.mc2.set_speed(2, -1 * speed)
        time.sleep(time1)
        self.stop_all_motors()

    def translate_left(self, speed, time1):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, -1 * speed)
        self.mc2.set_speed(2, speed)
        time.sleep(time1)
        self.stop_all_motors()

    def move_front_right(self, speed, time1):
        self.mc1.set_speed(1, 0)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, speed)
        self.mc2.set_speed(2, 0)
        time.sleep(time1)
        self.stop_all_motors()

    def move_back_right(self, speed, time1):
        self.mc1.set_speed(1, 0)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, -1 * speed)
        self.mc2.set_speed(2, 0)
        time.sleep(time1)
        self.stop_all_motors()

    def move_front_left(self, speed, time1):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, 0)
        self.mc2.set_speed(1, 0)
        self.mc2.set_speed(2, speed)
        time.sleep(time1)
        self.stop_all_motors()

    def move_back_left(self, speed, time1):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, 0)
        self.mc2.set_speed(1, 0)
        self.mc2.set_speed(2, -1 * speed)
        time.sleep(time1)
        self.stop_all_motors()

    def turn_right(self, speed, time1):
        self.mc1.set_speed(1, -1 * speed)
        self.mc1.set_speed(2, speed)
        self.mc2.set_speed(1, -1 * speed)
        self.mc2.set_speed(2, speed)
        time.sleep(time1)
        self.stop_all_motors()
        
    def turn_left(self, speed, time1):
        self.mc1.set_speed(1, speed)
        self.mc1.set_speed(2, -1 * speed)
        self.mc2.set_speed(1, speed)
        self.mc2.set_speed(2, -1 * speed)
        time.sleep(time1)
        self.stop_all_motors()

drivetrain = basic_X_drive()

try:
    drivetrain.move_forward(800, 1)
    drivetrain.move_reverse(800, 1)
    drivetrain.translate_right(800, 1)
    drivetrain.translate_left(800, 1)

except KeyboardInterrupt:
    pass
