# IncreaseWebCamFPS
Trying to get better FPS for Opencv

# Update info

2019/9/27 

Added `read_frames_slow.py` and `read_frames_fast.py` for benchmarking.

Credits to pyimg.

Updated both read_frames slow n fast just putting 10 seconds loop

Credits to https://stackoverflow.com/questions/44404093/timeout-for-10-seconds-while-loop-in-python

Results in `FPS_Resutls.ods`

So basically, sinlge core system won't be able to achieve better FPS.

However, it seems much more stable than cv2.VideoCapture.

Using imutils in multile core gives better results

# Author

Linuxkay
