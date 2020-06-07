import paho.mqtt.client as mqtt #import the client1
from multiprocessing import Process
import multiprocessing
import random
import threading
import time

class DeviceSignal:

    HOST="localhost"
    PORT=1883
    CLIENT_ID=""

    # ---- TOPICS NAME ---- 
    TEMPERATURE_TOPIC_NAME="/temperature" # 10 C between 25 C
    LIGHT_TOPIC_NAME="/light" # 10 between 800
    WATERFLOW_TOPIC_NAME="/waterflow" # 100 between 1000
    PH_TOPIC_NAME="/ph" # 0 between 14

    # ----- TOPICS MESSAGES ---
    WATERFLOW_TOPIC_MESSAGE="12" # create message per 10 seconds
    LIGTH_TOPIC_MESSAGE="400"
    PH_TOPIC_MESSAGE="7.13"
    TEMPERATURE_TOPIC_MESSAGE="23"

    client = None

    def connect(self,clientID=""):
        print("creating new instance")
        self.client = mqtt.Client(str(clientID)) #create new instance
        print("connecting to broker")
        self.client.connect(self.HOST,self.PORT) #connect to broker
        return self


    def generateTemperatureData(self):
        self.TEMPERATURE_TOPIC_MESSAGE = str("%.2f" % random.uniform(18,27))
        #print("GENERATED TEMPERATURE DATA: ",TEMPERATURE_TOPIC_MESSAGE)

    def generateLightData(self):
        self.LIGTH_TOPIC_MESSAGE = str("%.2f" % random.uniform(100,800))
        print("GENERATED LIGHT DATA: ",self.LIGTH_TOPIC_MESSAGE)

    def generateWaterflowData(self):
        self.WATERFLOW_TOPIC_MESSAGE = str("%.2f" % random.uniform(100,1000));
        print("GENERATED WATERFLOW DATA: ",self.WATERFLOW_TOPIC_MESSAGE)

    def generatePhData(self):
        self.PH_TOPIC_MESSAGE = str("%.2f" % random.uniform(0,14))
        print("GENERATED PH DATA: ",self.PH_TOPIC_MESSAGE)

    def publishTemperatureData(self):
        messageInfo = self.client.publish(self.CLIENT_ID+self.TEMPERATURE_TOPIC_NAME,self.TEMPERATURE_TOPIC_MESSAGE)
        timer = threading.Timer(3.0, self.generateTemperatureData) 
        timer.start() 


    def publishLightData(self):
        messageInfo = self.client.publish(self.CLIENT_ID+self.LIGHT_TOPIC_NAME,self.LIGTH_TOPIC_MESSAGE)
        timer = threading.Timer(3.0, self.generateLightData) 
        timer.start() 

    def publishWaterflowData(self):
        messageInfo = self.client.publish(self.CLIENT_ID+self.WATERFLOW_TOPIC_NAME,self.WATERFLOW_TOPIC_MESSAGE)
        timer = threading.Timer(3.0, self.generateWaterflowData) 
        timer.start() 

    def publishPhData(self):
        messageInfo = self.client.publish(self.CLIENT_ID+self.PH_TOPIC_NAME,self.PH_TOPIC_MESSAGE)
        timer = threading.Timer(3.0, self.generatePhData) 
        timer.start()


    def runDevice(self):
        while(True):
            self.publishTemperatureData()
            self.publishLightData()
            self.publishWaterflowData()
            self.publishPhData()
            time.sleep(3)



