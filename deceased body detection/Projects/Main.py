# import time
# import csv
# import serial
# from flask import Flask, render_template
# import numpy as np

# app = Flask(__name__)

# # Initialize serial connection for LiDAR
# lidar = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# # Function to read from LiDAR
# def read_lidar():
#     try:
#         distance = lidar.readline().decode('utf-8').strip()
#         return float(distance) if distance else None
#     except Exception as e:
#         print(f"Error reading LiDAR: {e}")
#         return None

# # Function to log data to CSV
# def log_data(timestamp, distance):
#     with open('sensor_data.csv', mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([timestamp, distance])

# # Flask route for the web interface
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Main loop to read data and log it
# def main_loop():
#     while True:
#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#         distance = read_lidar()
#         if distance is not None:
#             log_data(timestamp, distance)
#             print(f"Timestamp: {timestamp}, Distance: {distance} cm")
#         time.sleep(1)  # Adjust the sleep time as needed

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     from threading import Thread
#     Thread(target=main_loop).start()
#     app.run(host='0.0.0.0', port=5000)

