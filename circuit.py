'''

'''
import picamera
from Car import Car
import time

##### Settings #####
MAX_LEFT = 40
MAX_RIGHT = 40
TURN_SPEED = 90 

FORWARD_WAIT = 4
TURN_WAIT = .9
STEP_WAIT = 0.5

DEBUG = False
VIDEO_NAME = 'my_video.h264'

##### Camera Setup #####
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 60


def circ_leg(debug=False):
    # FORWARD
    car.control_car(MAX_LEFT, MAX_RIGHT)
    camera.wait_recording(FORWARD_WAIT)

    car.stop()
    camera.wait_recording(STEP_WAIT)
    
    # TURN
    car.control_car(TURN_SPEED, -TURN_SPEED)
    camera.wait_recording(TURN_WAIT)
    
    car.stop()
    camera.wait_recording(STEP_WAIT)

    if debug:
        time.sleep(2)
        # TURN
        car.control_car(-TURN_SPEED, TURN_SPEED)
        time.sleep(TURN_WAIT)
    
        car.stop()
        time.sleep(STEP_WAIT)


        # FORWARD
        car.control_car(-MAX_LEFT, -MAX_RIGHT)
        time.sleep(FORWARD_WAIT)

        car.stop()
        time.sleep(STEP_WAIT)

##### Car Setup #####
car = Car()
car.set_servo(1, 90)
time.sleep(0.5)
car.set_servo(2, 100)
time.sleep(0.5)

##### Circuit Execution #####
camera.start_recording(VIDEO_NAME)
camera.wait_recording(2)
car.control_car(MAX_LEFT, MAX_RIGHT)
camera.wait_recording(0.05)
if DEBUG:
    circ_leg(True)
else:
    for i in range(4):
        circ_leg()

car.stop()
camera.wait_recording(1)

##### Cleanup #####
camera.stop_recording()
del car
