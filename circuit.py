import picamera
from Car import Car
import time

MAX_SPEED = 75
TURN_SPEED = 100

def circ_leg():
    car.control_car(MAX_SPEED, MAX_SPEED)
    time.sleep(2)

    car.stop()
    time.sleep(.05)

    car.control_car(TURN_SPEED, -TURN_SPEED)
    time.sleep(.94)
    
    car.stop()
    time.sleep(.05)

# setup
car = Car()

# Go in circuit and record
# record
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 30
camera.start_recording('my_video.h264')

# circuit
car.control_car(MAX_SPEED, MAX_SPEED)
time.sleep(0.05)
for i in range(4):
    circ_leg()

car.stop()
camera.stop_recording()

del car
