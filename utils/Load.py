'''
Some shortcuts for loading/splicing video
'''
import cv2


def load(file_path):
    cap = cv2.VideoCapture(file_path)