from picamera
from Car import Car
import time

# setup
car = Car()

# Go in circle and record
# record
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')

# circle
car.control_car(50, 10)

time.sleep(3)

car.stop()
camera.stop_recording()

del car
