import picamera
from Car import Car
import time

def circ_leg():
    car.control_car(50, 50)
    time.sleep(3)
    car.control_car(50, -50)
    time.sleep(3)

# setup
car = Car()

# Go in circuit and record
# record
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 30
camera.start_recording('my_video.h264')

# circuit
for i in range(4):
    circ_leg()

car.stop()
camera.stop_recording()

del car
