
import sound
import threading
import travelingData
import brightness
import mousefeature

def activate(featureNo):
    travelingData.threadB = False
    if featureNo[0]==3:
        if travelingData.mouseOff:
            mouseThread=threading.Thread(target=mousefeature.mouseControl,name="mouse")
            mouseThread.start()

    threads=threading.Thread()
    if featureNo[0]==1:

        threads=threading.Thread(target=sound.soundControl,name='B')

    if featureNo[0]==2:


        threads = threading.Thread(target=brightness.brightnessControl,name='B')
    travelingData.threadB=False
    threads.start()



