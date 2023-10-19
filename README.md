# cs5510-visual-odometry
#### CS5510 Assignment 2: Visual Odometry Implementation

1. Implement Visual Odometry Algorithm

    - Task: Develop a Python program to compute the visual odometry of the robot.
    - Requirement: The program should be able to estimate the robot’s trajectory by analyzing the camera images.

    Our solution:

        [Files/packages/whatever used]

2. Navigate in a Circuit Around the Room

    - Task: Using the basic mobility commands, make the robot move in a circuit around the room (can be teleop). Record the video and process off-board, stream the video to an offboard device, or use internal compute to calculate VO.
    - Requirement: The circuit should be reasonably precise, and the robot should not drift significantly from the planned path. Record the video and odometry data from the robot's persepective.

###    Our solution:

Using circuit.py, the robot moves in a square circuit and records the video in 'my_video.h264'. Afterward, we download the video from the robot to be used in our implementation of Task 1.

###    Required packages and files:
- picamera
- time
- cv2
- smbus
- Car.py (whose github can be found [here](https://github.com/DIRECTLab/raspbot-code))

###    Instructions:

    1. Calibrate the robot
        a. Forward motion:
            i. Run `circuit.py` with variable `DEBUG` set to `True` 

            ii. Adjust MAX_LEFT and MAX_RIGHT to specify how fast each wheel should spin.

            iii. Repeat until the car moves forward in a straight line

        b. 90 degree turn:
            i. Run `circuit.py` with variable `DEBUG` set to `True`

            ii. Adjust TURN_WAIT and TURN_SPEED to specify the duration and speed of the turn respectively

            iii. Repeat until the car accurately completes a 90 degree turn

    2. Set variables
        a. Set `DEBUG` to False (if it isn't already)
        b. Adjust `FORWARD_WAIT` to specify the size of the square path the robot will take
        c. Adjust `VIDEO_NAME` to change the name of the recorded video

        NOTE: In order for the video to work with our implementation of orbslam, the extension of your video name must end in `.h264`
    3. Execute the program
        Place the robot in an open indoor area. On the robot, execute `circuit.py` and the robot will go forward for the previously specified amount of time and turn right.

    4. Download the video
        Our method of downloading the video was as follows:
        a. Obtain the path on your robot leading to the video file
        b. On the device you wish to download the video, type the following command into a bash shell:

            `scp pi@[robot_ip]:[path_to_file] [new_file_location]`

            ex: `scp pi@192.168.137.71:/home/pi/assn2/my_video.h264 .`

        In the above example, the file will be downloaded from the robot to your shell's current directory

    5. Load into orbslam
        TODO

3. Analyze and Report

    - Task: Analyze the recorded data and compare the estimated trajectory with the actual path taken by the robot. (You can use an estimate based on whatever)
    - Requirement: Submit a comprehensive report detailing your findings, methodology, any challenges faced, and possible improvements.

###     Our Analysis
TODO