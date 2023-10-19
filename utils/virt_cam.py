import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def video_publisher(video_file_path):
    rospy.init_node('camera_publisher', anonymous=True)
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    bridge = CvBridge()

    # Open the video file
    video_capture = cv2.VideoCapture(video_file_path)

    if not video_capture.isOpened():
        rospy.logerr("Video file not found or cannot be opened.")
        return

    rate = rospy.Rate(30)  # Adjust the publishing rate as needed

    while not rospy.is_shutdown():
        ret, frame = video_capture.read()

        if ret:
            try:
                # Convert the OpenCV image to a ROS image message
                ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
                # Publish the ROS image message to the specified topic
                image_pub.publish(ros_image)
            except CvBridgeError as e:
                rospy.logerr(e)

        rate.sleep()

    video_capture.release()

if __name__ == '__main__':
    try:
        # Specify the path to your video file here
        video_file_path = 'path/to/your/video/file.mp4'
        video_publisher(video_file_path)
    except rospy.ROSInterruptException:
        pass
    