from picamera2 import Picamera2
from Car import Car
import time
from multiprocessing import Process
import cv2

# setup
car = Car()

# Go in circle and record
picam2 = Picamera2()
picam2.start()

car.control_car(50, 10)
time.sleep(3)
car.stop()

circuit_pics = picam2.capture_array()

##### Write video #####
frame_size = (circuit_pics[0].shape[1], circuit_pics[0].shape[0])

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs like 'XVID' or 'MJPG' based on your needs
out = cv2.VideoWriter('circuit.mp4', fourcc, 30, frame_size)  # 30 frames per second, adjust as needed

# Loop through the image files and add them to the video
for image_file in circuit_pics:
    img = cv2.imread(image_file)
    out.write(img)

# Release the VideoWriter object and close the display window if any
out.release()
cv2.destroyAllWindows()

del car