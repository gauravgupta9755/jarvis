import math
import travelingData
import numpy

import camera
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)
minVol=volRange[0]
maxVol=volRange[1]

def soundControl():
    # print(camera.camera.handLandMarksCordinates)
    val=travelingData.threadB
    travelingData.threadB=True
    while(True):
        if travelingData.threadB == False:
            break
        lmList=camera.camera.handLandMarksCordinates
        if len(lmList)>0:
            x1,y1=lmList[4][1],lmList[4][2]
            x2,y2=lmList[8][1],lmList[8][2]
            lenght=math.hypot(x2-x1,y2-y1)

            # hand range 15 - 110
            # volume range -65 - 0
            vol=numpy.interp(lenght,[10,125],[minVol,maxVol])
            volume.SetMasterVolumeLevel(vol, None)