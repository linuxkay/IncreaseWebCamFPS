# https://qiita.com/iwatake2222/items/b8c442a9ec0406883950
# OpenCVのカメラ読み込みを高速化する

# -*- coding: utf-8 -*-
import sys
import time
import cv2

def decode_fourcc(v):
    # https://amdkkj.blogspot.com/2017/06/opencv-python-for-windows-playing-videos_17.html
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap = cv2.VideoCapture(1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('B', 'G', 'R', '3'));
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'));
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y', 'U', 'Y', 'V'));
print(decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC)))

if cap.isOpened() == False:
    print("cannot open")
    sys.exit(1)
_, img = cap.read() # dummy

cnt = 0
time_start = time.time()

try:
    while True:
        cnt += 1
        print(cnt)
        _, img = cap.read()
        # cv2.imshow('image', img)
        # key = cv2.waitKey(1)
        # if key == 27: # ESC
            # break
except KeyboardInterrupt:
    print("Exit loop by ctrl-c")

cap.release()
cv2.destroyAllWindows()
time_end = time.time()
print ("Capture time: {0}".format((time_end - time_start) * 1000 / cnt) + "[msec]")

