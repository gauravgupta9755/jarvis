import math
import travelingData
import  camera
import mouse
from win32api import GetSystemMetrics

print(GetSystemMetrics(0))
def mouseControl():
    
    travelingData.mouseOff=False
    
    while(True):
        # print(travelingData.mouseOff)
        if travelingData.mouseOff:
            break
        lmp=camera.camera.handLandMarksCordinates
       
        if(len(lmp)>0):
            mousex=lmp[8][1]
            mousey=lmp[8][2]
            print(abs(mousex-GetSystemMetrics(0)),mousey)
            mouse.move(mousex,mousey)



