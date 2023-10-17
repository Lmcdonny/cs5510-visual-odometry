'''
This is what runs on the robot
'''
from picamera2 import Picamera2
import YB_Pcb_Car
from multiprocessing import Process
from utils import init_net
from utils import Commands
from utils import Net_Info

##### Car Setup #####
car = YB_Pcb_Car.YB_Pcb_Car()
##### End Car Setup #####

##### Network Setup #####
# This is where you will put the ip of the ROBOT
server_socket, receive_socket = init_net.get_rec_sock(Net_Info.ROBOT_IP, Net_Info.CONTROL_PORT)

# This is where you will put the ip of your control device
send_socket = init_net.get_send_sock(Net_Info.CLIENT_IP, Net_Info.IMAGE_PORT)
##### End Network Setup #####

##### Operating Loop(s) #####
def send_loop():
    return

def rec_loop():
    while True:
        # Receive data from the client
        data = receive_socket.recv(1024)
        data = data.decode('utf-8')

        if data == Commands.FORWARD:
            car.Car_Run(150, 150)
        elif data == Commands.LEFT:
            car.Car_Left(0, 150)
        elif data == Commands.BACKWARD:
            car.Car_Back(150,150)
        elif data == Commands.RIGHT:
            car.Car_Right(150, 0)
        elif data == Commands.STOP:
            car.Car_Stop()
        elif data == Commands.QUIT:
            car.Car_Stop()
            break


image_loop = Process(target=send_loop)
control_loop = Process(target=rec_loop)

image_loop.start()
control_loop.start()

image_loop.join()
control_loop.join()
##### End Operating Loop(s) #####

##### Cleanup #####
# Close the client and server sockets
receive_socket.close()
server_socket.close()

# Terminate the car with extreme prejudice
del car
##### End Cleanup #####