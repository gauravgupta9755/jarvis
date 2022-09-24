import mediapipe as mp
import time
import cv2
# create class for handdector ---
# it have two function --
# 1-> findHands ---> it find the hands and draw the landmarks drfaulst draw is true
#       it has two parameter first is img(image) and second is draw(bool)(optional)(default is True)
#       it will return the img as landmarks

# 2-> findPosition -->> it find the position of all 21 landmarks and return the list of landmarks id,x-position and y-position
#       it has three parameter img(image),handNo(int)(optional)(default is 0) and draw(bool)(optional)(default is True)
class handDector():
    def __init__(self,mode=False,maxHands=2, model_complexity=1,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.model_complexity=model_complexity

        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.model_complexity,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils


    # function ------  1.
    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)


        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img



    # function -------->2.
    def findPosition(self,img,handNo=0,draw=True):
        lmList=[]


        if self.results.multi_hand_landmarks:
            myHands = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHands.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
        return lmList




