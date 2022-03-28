from datetime import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.now().strftime('%Y-%m-%d  %H-%M-%S')
print(time_stamp)
print(width, height)
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('d', 'o', 'l', 'a')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
webcam = cv2.VideoCapture(0)

while True:
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    image_np = np.array(image)
    image_final = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    frame_height, frame_width, _ =frame.shape
    image_final[0: frame_height, 0: frame_width, :] = frame[0: frame_height, 0: frame_width :]
    print(frame_width,frame_height)
    cv2.imshow('Secret Capture', image_final)

    captured_video.write(image_final)
    if cv2.waitKey(10) == ord('s'):
        break
