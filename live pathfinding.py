import mss
from PIL import Image, ImageGrab
import pyautogui

import cv2
import numpy as np
import time

w, h = pyautogui.size()
print("PIL Screen Capture Speed Test")
print("Screen Resolution: " + str(w) + 'x' + str(h))

img = None
t0 = time.time()
n_frames = 1
monitor = {"top": 0, "left": 0, "width": w, "height": h}
with mss.mss() as sct:
    while True:
        img = sct.grab(monitor)
        img = np.array(img)  # Convert to NumPy array
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR color

        small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

        height, width = small.shape[:2]

        # Desired "pixelated" size
        w, h = (500, 500)

        # Resize input to "pixelated" size
        temp = cv2.resize(small, (w, h), interpolation=cv2.INTER_BITS)

        # Initialize output image
        output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

        cv2.imshow("Computer Vision", small)
        cv2.imshow("Computer pixe;", output)

        # Break loop and end test
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        elapsed_time = time.time() - t0
        avg_fps = (n_frames / elapsed_time)
        print("Average FPS: " + str(avg_fps))
        n_frames += 1
