import threading
import htm
import vtm
import  tvm
import  cv2
import feature
import execute
import os
from gtts import gTTS
import tvm
voiceText=vtm.voiceToText(features=feature.features,device_index=5);

while(True):
    text=voiceText.VtoT()
    print(text)

    if text:

        featureNo=voiceText.GetFeature()
        if(featureNo!=-1 and featureNo[1]=="start"):
            myobj = gTTS(text="hello sir I am lena how can I help you", lang="en", slow=False)
            myobj.save("my.mp3")
            tvm.play()
            while(True):
                text = voiceText.VtoT()
                print(text)
                featureNo = voiceText.GetFeature()
                if text:

                    if featureNo ==-1:
                        print("sir your command is not matching in our added features")
                        mytext = "sir your command is not matching in our added features"
                        myobj = gTTS(text=mytext, lang="en", slow=False)
                        myobj.save("my.mp3")
                        tvm.play()
                    else:
                        print(featureNo[1])
                        if feature.notfeatures.get(featureNo[1])==None:
                            mytext= featureNo[1]+"feature activated"
                            myobj = gTTS(text=mytext, lang="en", slow=False)
                            myobj.save("my.mp3")

                            tvm.play()
                        if featureNo[1]=="stop":
                            myobj = gTTS(text="thanks sir, how was your experience please share", lang="en", slow=False)
                            myobj.save("my.mp3")
                            tvm.play()
                            break


                       # t1 = threading.Thread(target=execute.executing, args=(featureNo))

        if (featureNo != -1 and featureNo[1] == "over"):
            break