#https://stackoverflow.com/questions/51097725/cv2-videowriter-in-rpi3-is-faster-than-actual/51098900
import numpy as np
from skvideo import io
import cv2, sys
import time
import os

if __name__ == '__main__':

    file_name = 'video_clip.avi'

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoOut = cv2.VideoWriter(file_name, fourcc, 30.0, (640, 352))
    cap = cv2.VideoCapture("http://192.168.0.100/cgi-bin/hi3510/snap.cgi?&-getstream.cgi")

    if not cap.isOpened() or not videoOut.isOpened():
        exit(-1)

    start_time = time.time()
    frame_count = 0
    duration = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print('empty frame')
            break
        videoOut.write(frame)  # write each frame to make video clip
        frame_count += 1

        duration = time.time()-start_time
        if int(duration) == 10:
            videoOut.release()
            cap.release()
            break

    actualFps = np.ceil(frame_count/duration)

    os.system('ffmpeg -y -i {} -c copy -f h264 tmp.h264'.format(file_name))
    os.system('ffmpeg -y -r {} -i tmp.h264 -c copy {}'.format(actualFps,file_name))
