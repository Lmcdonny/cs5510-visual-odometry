'''
Some shortcuts for loading/splicing video
'''
import cv2

def load(file_path):
    cap = cv2.VideoCapture(file_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    frames = []

    # Loop through the video and read each frame
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break  # Break the loop when we reach the end of the video
        
        # You can process or store the frame here
        # For example, you can append it to the frames list
        frames.append(frame)

    # Release the VideoCapture object and close the video file
    cap.release()

    return frames