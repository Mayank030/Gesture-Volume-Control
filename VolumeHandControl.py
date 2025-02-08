# Importing Libraries
import time
import cv2
import numpy as np
import HandTrackingModule as htm
import math

# Imports for Volume Control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# pycaw stands for Python Core Audio Windows Library


################################
wCam, hCam = 640, 480      # The dimensions of the Window
################################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


detector = htm.handDetector(detectionCon=0.7)



# For Volume Control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()      # The range is -65(min) to 0(max)
minVol = volRange[0]
maxVol = volRange[1]


vol = 0
volBar = 400
volPer = 0


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])        # ID of Thumb and Index Finger

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2      # The center of the line between thumb and index

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)   # For index finger
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)   # For Thumb
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)        # Drawing the line between thumb and index
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)   # For center of the line

        length = math.hypot(x2 - x1, y2 - y1)     # The length of the line to alter the volume using hypotenuse function
        # print(length)
        # Hand range 50 to 300
        # Volume Range -65 to 0
        
        # Setting the Hand Range to Volume Range

        vol = np.interp(length, [50, 300], [minVol, maxVol])   # linear interpolation
        volBar = np.interp(length, [50, 300], [400, 150])   # For volume bar
        volPer = np.interp(length, [50, 300], [0, 100])     # Volume Percentage
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)   # Changing the color when the length is less (than 50)

    # Displaying the Volume Bar 

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    cv2.imshow("volume Control", img)
    cv2.waitKey(1)