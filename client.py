'''
This is what you run to control the robot.
'''
from pynput import keyboard
from utils import Commands
from utils import init_net
from utils import Net_Info

##### Network Setup #####
# This is where you will put the ip of the ROBOT
send_socket = init_net.get_send_sock(Net_Info.ROBOT_IP, Net_Info.CONTROL_PORT)

# This is where you will put the ip of your control device
rec_socket = init_net.get_rec_sock(Net_Info.CLIENT_IP, Net_Info.IMAGE_PORT)
##### End Network Setup #####

###### Control Commands #####
curr_command = None
def on_press(key):
    global curr_command
    message = None

    try:
        if key.char == 'w':
            if curr_command != Commands.FORWARD:
                message = Commands.FORWARD
                curr_command = Commands.FORWARD
        elif key.char == 's':
            if curr_command != Commands.BACKWARD:
                message = Commands.BACKWARD
                curr_command = Commands.BACKWARD
        elif key.char == 'a':
            if curr_command != Commands.LEFT:
                message = Commands.LEFT
                curr_command = Commands.LEFT
        elif key.char == 'd':
            if curr_command != Commands.RIGHT:
                message = Commands.RIGHT
                curr_command = Commands.RIGHT
    except AttributeError:
        pass

    if message != None:
        send_socket.send(message.encode('utf-8'))
        
def on_release(key):
    global curr_command
    if key == keyboard.Key.esc:
        print('Quitting...')
        send_socket.send(Commands.QUIT.encode('utf-8'))
        return False
    
    message = Commands.STOP
    if curr_command != message:
        send_socket.send(message.encode('utf-8'))
        curr_command = Commands.STOP
###### End Control Commands #####  

##### Operating Loop(s) #####
'''
This is in charge of sending commands to the robot
'''
def send_loop():
    # Pynput listener
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

'''
This is in charge of receiving images from the robot
'''
def rec_loop():
    return


##### End Operating Loop(s) #####

##### Cleanup #####
# Close the client socket
send_socket.close()
rec_socket.close()
##### End Cleanup #####