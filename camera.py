import math
import imutils
import htm
import cv2
import threading
import travelingData
from win32api import GetSystemMetrics


class Camera():

    handLandMarksCordinates=[]
    def __init__(self):
        self.handLandMarksCordinates=[]
    def cameraActivate(self):
        print("this is a new thread for in camera");
        handDetect = htm.handDector()
        vid = cv2.VideoCapture(3)

        while (True):
            if travelingData.x==False:
                break
            ret, frame = vid.read()
            if ret:
                frame=imutils.resize(frame,width=GetSystemMetrics(0))
                handDetect.findHands(frame)
                self.handLandMarksCordinates= handDetect.findPosition(img=frame,draw=False)
                # frame=cv2.flip(frame,1)
                cv2.imshow('frame', frame)
                # if len(self.handLandMarksCordinates)>0:
                #     lmp=self.handLandMarksCordinates
                #     x1, y1 = lmp[4][1], lmp[4][2]
                #     x2, y2 = lmp[5][1], lmp[5][2]
                #     print(math.hypot(x2 - x1, y2 - y1))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

camera=Camera()

def setHandLandMarks ():
    camera.cameraActivate()
