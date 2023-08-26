from picamera2 import Picamera2, Preview
from libcamera import controls
import numpy as np
import time
import os

os.environ["LIBCAMERA_LOG_LEVELS"] = "3"

picam = Picamera2()
    
# config = picam.create_still_configuration()
config = picam.create_preview_configuration(main={"size": (1920, 1080)})
picam.configure(config)

picam.start_preview(Preview.QTGL, x=0, y=0, width=1920, height=1080)

# picam._preview.qpicamera2.setWindowFlags(picam._preview.qpicamera2.windowFlags(
# ) | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

# overlay = np.zeros((300, 400, 4), dtype=np.uint8)
# overlay[:150, 200:] = (255, 0, 0, 64)
# overlay[150:, :200] = (0, 255, 0, 64)
# overlay[150:, 200:] = (0, 0, 255, 64)

# overlay = np.zeros((200, 200, 4), dtype=np.uint8)
# overlay[:100, 100:] = (255, 0, 0, 64)  # red
# overlay[100:, :100] = (0, 255, 0, 64)  # green
# overlay[100:, 100:] = (0, 0, 255, 64)  # blue

a = np.zeros((1080, 1920, 4), dtype=np.uint8)
a[540, :, :] = 0xff
a[:, 960, :] = 0xff


# picam.set_overlay(overlay)

o = picam.set_overlay(a)

picam.start()

while True:
    time.sleep(5)
    
picam.remove_overlay(o)
picam.close()
