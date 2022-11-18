import math
import threading

import numpy
import screen_brightness_control as sbc
import travelingData
import camera
from sound import volume

# get the brightness
brightness = sbc.get_brightness()
# get the brightness for the primary monitor
primary = sbc.get_brightness()

# set the brightness to 100%
sbc.set_brightness(50)



minBright=0
maxBright=100
def brightnessControl():
    # print(camera.camera.handLandMarksCordinates)

    travelingData.threadB = True
    while(True):

        if travelingData.threadB ==False:
            break
        lmList=camera.camera.handLandMarksCordinates
        if len(lmList)>0:
            x1,y1=lmList[4][1],lmList[4][2]
            x2,y2=lmList[8][1],lmList[8][2]
            lenght=math.hypot(x2-x1,y2-y1)

            # hand range 20 - 110
            # bright range 0 - 100
            bright=numpy.interp(lenght,[20,125],[minBright,maxBright])
            sbc.set_brightness(bright)