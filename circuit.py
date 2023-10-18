from picamera import Picamera
from picamera.encoders import H264Encoder
from picamera.outputs import FileOutput
from Car.py import Car
import time

# setup
car = Car()

# Go in circle and record
# record
picam = Picamera()
video_config = picam.create_video_configuration()
picam.configure(video_config)
encoder = H264Encoder(bitrate=10000000)
output = FileOutput('test.h264')
picam.start_recording(encoder, output)

# circle
car.control_car(50, 10)

time.sleep(3)

car.stop()
picam2.stop_recording()

del car
