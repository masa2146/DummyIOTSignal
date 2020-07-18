import paho.mqtt.client as mqtt  # import the client1
from multiprocessing import Process
import multiprocessing
import random
import threading
import time
import json
import datetime


class DeviceSignal:

    HOST = "localhost"
    PORT = 1883
    CLIENT_ID = "5ef6e3b50810e92c8fa198dd-"

    # ---- TOPICS NAME ----
    TEMPERATURE_TOPIC_NAME = "temperature"  # 10 C between 25 C
    LIGHT_TOPIC_NAME = "light"  # 10 between 800
    WATERFLOW_TOPIC_NAME = "waterflow"  # 100 between 1000
    PH_TOPIC_NAME = "ph"  # 0 between 14

    # ----- TOPICS MESSAGES ---
    WATERFLOW_TOPIC_MESSAGE = "12"  # create message per 10 seconds
    LIGTH_TOPIC_MESSAGE = "400"
    PH_TOPIC_MESSAGE = "7.13"
    TEMPERATURE_TOPIC_MESSAGE = "23"

    client = None

    def connect(self, clientID=""):
        print("creating new instance")
        self.client = mqtt.Client(str(clientID))  # create new instance
        print("connecting to broker")
        self.client.connect(self.HOST, self.PORT)  # connect to broker
        return self

    def generateTemperatureData(self):
        self.TEMPERATURE_TOPIC_MESSAGE = str("%.2f" % random.uniform(18, 27))
        # print("GENERATED TEMPERATURE DATA: ",TEMPERATURE_TOPIC_MESSAGE)

    def generateLightData(self):
        self.LIGTH_TOPIC_MESSAGE = str("%.2f" % random.uniform(100, 800))
        

    def generateWaterflowData(self):
        self.WATERFLOW_TOPIC_MESSAGE = str("%.2f" % random.uniform(100, 1000));
        

    def generatePhData(self):
        self.PH_TOPIC_MESSAGE = str("%.2f" % random.uniform(0, 14))
        

    def publishTemperatureData(self):
        MQTT_MSG = json.dumps({"data": self.TEMPERATURE_TOPIC_MESSAGE, "date": str(datetime.datetime.now())})
        messageInfo = self.client.publish(
            self.CLIENT_ID+self.TEMPERATURE_TOPIC_NAME, MQTT_MSG)
        print("PUBLISHED TEMPERATURE DATA: ",MQTT_MSG)
        timer = threading.Timer(3.0, self.generateTemperatureData)
        timer.start()


    def publishLightData(self):
        MQTT_MSG = json.dumps({"data": self.LIGTH_TOPIC_MESSAGE, "date": str(datetime.datetime.now())})
        messageInfo = self.client.publish(
            self.CLIENT_ID+self.LIGHT_TOPIC_NAME, MQTT_MSG)
        print("PUBLISHED LIGHT DATA: ", MQTT_MSG)
        timer = threading.Timer(3.0, self.generateLightData)
        timer.start()

    def publishWaterflowData(self):
        MQTT_MSG = json.dumps({"data": self.WATERFLOW_TOPIC_MESSAGE, "date": str(datetime.datetime.now())})
        messageInfo = self.client.publish(
            self.CLIENT_ID+self.WATERFLOW_TOPIC_NAME, MQTT_MSG)
        print("PUBLISHED WATERFLOW DATA: ", MQTT_MSG)
        timer = threading.Timer(3.0, self.generateWaterflowData)
        timer.start()

    def publishPhData(self):
        MQTT_MSG = json.dumps({"data": self.PH_TOPIC_MESSAGE, "date": str(datetime.datetime.now())})
        messageInfo = self.client.publish(
            self.CLIENT_ID+self.PH_TOPIC_NAME, MQTT_MSG)
        print("PUBLISHED PH DATA: ", MQTT_MSG)
        timer = threading.Timer(3.0, self.generatePhData)
        timer.start()


    def runDevice(self):
        while(True):
            self.publishTemperatureData()
            self.publishLightData()
            self.publishWaterflowData()
            self.publishPhData()
            time.sleep(3)
