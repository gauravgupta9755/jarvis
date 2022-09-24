import cv2 as cv
import numpy as np
import datetime
import mediapipe as mp
import time
import htm


# read and write image--------------


# img = cv.imread('lena.jpg',-1)
# cv.imshow('image',img)
# k=cv.waitKey(0) & 0xFF
# if k==27:
#     cv.destroyAllWindows()
# elif k== ord('s'):
#     cv.imwrite('lena_copy.png',img)
#     cv.destroyAllWindows()








#  read and write video ----------------


# cap = cv.VideoCapture(2)
# fourcc=cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi',fourcc,30.0,(640,480))
# print(cap.isOpened())
# while cap.isOpened() :
#     ret, frame = cap.read()
#     if ret == True :
#         print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
#         out.write(frame)
#         gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#         cv.imshow("frame", gray)
#
#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break
#     else :
#         break
#
#
#
#
# cap.release()
# out.release()
# cv.destroyAllWindows()
#


# img = cv.imread('lena.jpg',1)
# img=cv.line(img,(0,0),(300,300),(0,255,0),5)
# img=cv.rectangle(img,(0,0),(255,255),(0,0,255),-1)
# img=cv.circle(img,(400,400),60,(255,0,0),3)
# font=cv.FONT_HERSHEY_SIMPLEX
# img=cv.putText(img,"gaurav",(100,100),font,4,(255,255,255),10,cv.LINE_AA)
# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroAllWindows()
#
#
# cap=cv.VideoCapture(2)
# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# cap.set(3,3000)
# cap.set(4,3000)
# print(cap.get(3))
# print(cap.get(4))
# while (cap.isOpened()):
#     ret,frame=cap.read()
#     if ret==True:
#         # gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#         cv.imshow('frame',frame)
#
#         if cv.waitKey(1)& 0xFF==ord('q'):
#             break;
#     else:
#         break
# cap.release()
# cv.destroyAllWindows()

#
# cap=cv.VideoCapture(2)
# cap.set(3,3000)
# cap.set(4,4000)
#
# while (cap.isOpened()):
#     ret,frame =cap.read()
#     if ret ==True:
#         font = cv.FONT_HERSHEY_SIMPLEX
#         text="Width "+ str(cap.get(3)) + " Height " + str(cap.get(4))
#         datet= str(datetime.datetime.now())
#         frame=cv.putText(frame,datet,(10,50),font,1,(0,255,255),4,cv.LINE_AA)
#         cv.imshow('frame',frame)
#
#         if cv.waitKey(1)& 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# cv.destroyAllWindows()
#




# find to cordinate on click event------

# events= [i for i in dir(cv) if 'EVENT' in i]
# print(events)
#
# def click_event (event,x,y,flags,param):
#     if event==cv.EVENT_LBUTTONDOWN:
#         print(x," , ",y)
#         font =cv.FONT_HERSHEY_SIMPLEX
#         strxy= str(x)+','+str(y)
#         cv.putText(img,strxy,(x,y),font,1,(255,0,0),3)
#         cv.imshow('image',img)
#     if event== cv.EVENT_RBUTTONDOWN:
#         blue=img[y,x,0]
#         green=img[y,x,1]
#         red=img[y,x,2]
#         font=cv.FONT_HERSHEY_SIMPLEX
#         strBGR=str(blue)+','+str(green)+','+str(red)
#         cv.putText(img,strBGR,(x,y),font,0.4,(0,255,0),1)
#         cv.imshow('image', img)
#
# # img=np.zeros((512,512,3),np.uint8)
# img= cv.imread("lena.jpg")
# cv.imshow('image',img)
# cv.setMouseCallback('image',click_event)
# cv.waitKey(0)
# cv.destroyAllWindows()


# draw the line with click mouse events-----
# def click_event (event,x,y,flags,param):
#     if event== cv.EVENT_LBUTTONDOWN:
#         cv.circle(img,(x,y),3,(0,0,255),-1)
#         cv.imshow('image',img)
#         points.append((x,y))
#         if len(points)>=2:
#             cv.line(img,points[-1],points[-2],(255,0,0),5)
#             cv.imshow('image',img)
#
#
# # img = cv.imread('lena.jpg')
# img= np.zeros((512,512,3))
# cv.imshow('image',img)
# points=[]
# cv.setMouseCallback('image',click_event)
# cv.waitKey(0)
# cv.destroyAllWindows()
#

pTime = 0
cTime = 0
detector = htm.handDector()
cap = cv.VideoCapture(2)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, 0, False)
    if len(lmList) != 0:
        print(lmList[4])
    img = cv.flip(img, 1)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 50), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
