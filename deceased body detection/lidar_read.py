import csv
import serial
import time

# Configure the serial port (adjust the port and baud rate as necessary)
SERIAL_PORT = '/dev/ttyUSB0'  # Change this to your LiDAR's serial port
BAUD_RATE = 115200  # Change this to your LiDAR's baud rate

def read_lidar():
    try:
        # Initialize the serial connection
        lidar = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("LiDAR initialized. Reading data...")

        # Open a CSV file for logging
        with open('lidar_data.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Timestamp', 'Distance (cm)'])  # Write header

            while True:
                # Read a line from the LiDAR
                line = lidar.readline().decode('utf-8').strip()
                if line:
                    try:
                        # Assuming the LiDAR sends distance in cm
                        distance = float(line)
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Timestamp: {timestamp}, Distance: {distance} cm")
                        
                        # Write the timestamp and distance to the CSV file
                        writer.writerow([timestamp, distance])
                        csvfile.flush()  # Ensure data is written to the file
                    except ValueError:
                        print(f"Invalid distance value: {line}")
                time.sleep(0.1)  # Adjust the sleep time as needed

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        lidar.close()

if __name__ == '__main__':
    read_lidar()