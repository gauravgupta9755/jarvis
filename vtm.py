
import  speech_recognition as sr

import re






class voiceToText():
    r = sr.Recognizer()


    def __init__(self,energy_threshold=300,dynamic_energy_threshold = True,dynamic_energy_adjustment_damping = 0.15,
                 dynamic_energy_ratio = 1.5,pause_threshold = 0.8,operation_timeout = None,phrase_threshold = 0.3,non_speaking_duration = 0.5,device_index=0,features={},textList=[]):

        self.energy_threshold = energy_threshold  # minimum audio energy to consider for recording
        self.dynamic_energy_threshold = dynamic_energy_threshold
        self.dynamic_energy_adjustment_damping = dynamic_energy_adjustment_damping
        self.dynamic_energy_ratio = dynamic_energy_ratio
        self.pause_threshold =pause_threshold  # seconds of non-speaking audio before a phrase is considered complete
        self.operation_timeout = operation_timeout  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        self.phrase_threshold = phrase_threshold  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        self.non_speaking_duration = non_speaking_duration # seconds of non-speaking audio to keep on both sides of the recording
        self.device_index=device_index
        self.features=features # feature list which is performe
        self.textList=textList # store all features index which using or used
    def VtoT(self):

            # Exception handling to handle
            # exceptions at the runtime
            try:
                # use the microphone as source for input.
                with sr.Microphone(self.device_index) as source:
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level

                    self.r.adjust_for_ambient_noise(source, duration=0.5)

                    # listens for the user's input
                    print("speak now---")
                    audio = self.r.listen(source)

                    # Using google to recognize audio
                    MyText = self.r.recognize_google(audio)
                    MyText = MyText.lower()
                    res = re.findall(r'\w+', MyText)

                    for i in res:
                        indxex=self.features.get(i)
                        if(indxex!=None):
                            self.textList.append((indxex,i))
                            break
                    else:
                        self.textList.append(-1)
                return MyText

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return None

            except sr.UnknownValueError:
                print("NA voice")
                return None



    # it will return the feature index......
    def GetFeature(self,textListIndex=-1):
        if(textListIndex==-1):
            textListIndex=len(self.textList)-1
        if(textListIndex<0 or textListIndex>=len(self.textList) ) :
            return None
        return self.textList[textListIndex]




