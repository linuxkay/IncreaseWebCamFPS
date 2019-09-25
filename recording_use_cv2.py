import numpy as np
import cv2

cap = cv2.VideoCapture("http://192.168.0.100/cgi-bin/hi3510/snap.cgi?&-getstream.cgi")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/tmp/output.avi',fourcc, 20.0, (640,352))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
