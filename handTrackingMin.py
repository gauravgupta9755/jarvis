import mediapipe as mp
import  cv2
import time



cap=cv2.VideoCapture(2)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0

while cap.isOpened() :
    ret, img = cap.read()
    if ret == True :

        # flip the image ----->>>
        img = cv2.flip(img, 1)

         # change space color into COLOR_BGR2RGB------>>>
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=hands.process(imgRGB)


        # DRAW THE LANDMARKS -------->>>>
        if results.multi_hand_landmarks :
            for handLms in results.multi_hand_landmarks:
                for id,lm in enumerate(handLms.landmark):
                    # print(id,lm)
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    print(id,cx,cy)

                    # draw circle in specific landmark ------------------------------->>>
                    if id==0:
                        cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


        # GET FPS WITH USE TIME OBJECT --------  WITH CURRENT TIME AND PREVIOUS TIME------>>
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),4,cv2.LINE_AA)



        # SHOW IMAGE IN WINDOW ----------->>>>>>>>
        cv2.imshow("frame", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break




cap.release()
cv2.destroyAllWindows()