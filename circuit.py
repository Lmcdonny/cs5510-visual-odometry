from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from Car import Car
import time

# setup
car = Car()

# Go in circle and record
# record
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(bitrate=10000000)
output = FileOutput('test.h264')
picam2.start_recording(encoder, output)

# circle
car.control_car(50, 10)

time.sleep(3)

car.stop()
picam2.stop_recording()

del car