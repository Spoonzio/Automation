import cv2
import time
from PIL import Image

# Assign camera to source
camera = cv2.VideoCapture(0)

while True:
    # Capture Frame
    _ , frame = camera.read()
    if frame is None:
        break

    # Play frames
    # time.sleep(0.25)
    cv2.imshow("Camera", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Exit 
camera.release()
cv2.destroyAllWindows()