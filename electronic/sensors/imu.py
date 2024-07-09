import smbus
import time
import math

# Define I2C bus number (1 on Raspberry Pi 3+ and 4, 0 on earlier models)
bus = smbus.SMBus(1)

# MPU-6050 register addresses
MPU6050_ADDR = 0x68  # MPU-6050 I2C address
MPU6050_REG_GYRO_ZOUT_H = 0x47    # Gyroscope Z-axis data registers

# Initialize MPU-6050
def init_mpu6050():
    bus.write_byte_data(MPU6050_ADDR, 0x6B, 0x00)  # Wake up MPU-6050

# Read raw gyroscope values (Z-axis only for this example)
def read_gyro_raw():
    data = bus.read_i2c_block_data(MPU6050_ADDR, MPU6050_REG_GYRO_ZOUT_H, 2)
    gyro_raw = (data[0] << 8 | data[1])  # Gyroscope Z-axis
    # Convert to signed value
    if gyro_raw > 32767:
        gyro_raw -= 65536
    return gyro_raw

# Convert raw value to degrees per second for gyroscope
def convert_gyro_data(raw_value):
    return raw_value / 131.0  # MPU-6050 sensitivity scale factor for gyro Z-axis

# Calculate angle of rotation around Z-axis based on gyroscope data
def calculate_rotation_angle(gyro_data, delta_t):
    # Convert gyro data to degrees per second
    gyro_deg_per_sec = gyro_data

    # Integrate angular velocity to calculate angle (rotation) around Z-axis
    angle_change = gyro_deg_per_sec * delta_t

    return angle_change

# Main program
def main():
    init_mpu6050()

    last_time = time.time()
    angle_z = 0.0

    while True:
        current_time = time.time()
        delta_t = current_time - last_time

        gyro_raw = read_gyro_raw()
        gyro_data = convert_gyro_data(gyro_raw)

        # Calculate angle change around Z-axis
        angle_change = calculate_rotation_angle(gyro_data, delta_t)
        angle_z += angle_change

        print(f"Angle of rotation around Z-axis (degrees): {angle_z:.2f}")

        last_time = current_time

        time.sleep(0.1)  # Adjust delay as needed

if __name__ == "__main__":
    main()
