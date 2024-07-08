import motoron
import time

class XDriveRobot:
    def __init__(self, kp, ki, kd):
        self.mc = motoron.MotoronI2C()
        self.configure_motors()
        self.mc.reinitialize()
        self.mc.disable_crc()
        
        # PID parameters
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        # PID state variables
        self.prev_error_x = 0
        self.prev_error_y = 0
        self.prev_error_theta = 0
        self.integral_x = 0
        self.integral_y = 0
        self.integral_theta = 0
        
    def configure_motors(self):
        # Configure motor 1 - front right
        self.mc.set_max_acceleration(1, 140)
        self.mc.set_max_deceleration(1, 300)
        
        # Configure motor 2 - front left
        self.mc.set_max_acceleration(2, 140)
        self.mc.set_max_deceleration(2, 300)
        
        # Configure motor 3 - back right
        self.mc.set_max_acceleration(3, 140)
        self.mc.set_max_deceleration(3, 300)
        
        # Configure motor 4 - back left
        self.mc.set_max_acceleration(4, 140)
        self.mc.set_max_deceleration(4, 300)
    
    def stop_all_motors(self):
        self.mc.set_speed(1, 0)
        self.mc.set_speed(2, 0)
        self.mc.set_speed(3, 0)
        self.mc.set_speed(4, 0)

    def set_motor_speeds(self, vx, vy, omega):
        # Convert velocities to motor speeds
        self.mc.set_speed(1, int(vx - vy - omega))
        self.mc.set_speed(2, int(vx + vy + omega))
        self.mc.set_speed(3, int(vx - vy + omega))
        self.mc.set_speed(4, int(vx + vy - omega))

    def get_current_position(self):
        # Replace with actual code to get the robot's current position
        return (0, 0, 0)

    def pid_control(self, target_x, target_y, target_theta, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            current_x, current_y, current_theta = self.get_current_position()
            
            # Calculate errors
            error_x = target_x - current_x
            error_y = target_y - current_y
            error_theta = target_theta - current_theta
            
            # Update integrals
            self.integral_x += error_x
            self.integral_y += error_y
            self.integral_theta += error_theta
            
            # Calculate derivatives
            derivative_x = error_x - self.prev_error_x
            derivative_y = error_y - self.prev_error_y
            derivative_theta = error_theta - self.prev_error_theta
            
            # PID outputs
            vx = self.kp * error_x + self.ki * self.integral_x + self.kd * derivative_x
            vy = self.kp * error_y + self.ki * self.integral_y + self.kd * derivative_y
            omega = self.kp * error_theta + self.ki * self.integral_theta + self.kd * derivative_theta
            
            # Update previous errors
            self.prev_error_x = error_x
            self.prev_error_y = error_y
            self.prev_error_theta = error_theta
            
            # Set motor speeds based on PID outputs
            self.set_motor_speeds(vx, vy, omega)
            
            time.sleep(0.01)
        
        self.stop_all_motors()

robot = XDriveRobot(kp=1.0, ki=0.1, kd=0.05)

try:
    # Move to position (10, 5, 0) over 5 seconds
    robot.pid_control(10, 5, 0, 5)
except KeyboardInterrupt:
    robot.stop_all_motors()
