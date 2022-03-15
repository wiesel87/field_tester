import statistics
import json
import random
import threading
import time
import sqlite3
import datetime
import base64
from tkinter import Label

from paho.mqtt import client as mqtt_client

from api import getTotalDevices
import GUI


class Sensor:
    def __init__(self, name):
        self.name = name
        self.number = 0
        self.RSSI = []
        self.SNR = []
        self.battery = 0
        self.connected = False

    def addMeasurement(self, RSSI, SNR):
        self.RSSI.append(RSSI)
        self.SNR.append(SNR)
        self.number = self.number + 1


sensors = []

broker = "192.168.1.171"  # Sani Nudge
# broker = 'localhost'
port = 1883
topic = "application/1/device/+/event/up"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = ''
password = ''

TempMeasRSSI = []
TempMeasSNR = []
TimePerc = 0
IsMeassuring = False
battery_scan_finished = False
MQTT_output = ""
MQTT_output_data = []

total_devices = 0


############################################ MQTT:  #####################################################
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe_scan(client: mqtt_client):
    client.subscribe(topic)
    client.on_scan_message = on_scan_message


def subscribe_battery(client: mqtt_client):
    client.subscribe(topic)
    client.on_message = on_battery_message


############################################ MQTT: subscribe #####################################################

def on_battery_message(client, userdata, msg):
    global sensors
    global battery_scan_finished
    # print(f"Received `{msg.payload.decode()}` ")
    theString = str(msg.payload.decode("utf-8"))
    # print(theString)
    msg_a = json.loads(theString)

    sensorName = str(msg_a['deviceName'])
    frameCounter = str(msg_a['fCnt'])
    payload = base64.b64decode(msg_a['data']).hex()
    messageType = payload[8:10]
    battery = int(payload[12:14], 16)

    sensors_connected = 0

    exists = False
    for x in range(len(sensors)):
        if sensors[x].name == sensorName:
            exists = True

    if not exists:
        new_sensor = Sensor(sensorName)
        sensors.append(new_sensor)

    for x in range(len(sensors)):
        if frameCounter == "0" and sensors[x].name == sensorName:
            sensors[x].battery = battery
            print(sensors[x].name + " battery is " + str(sensors[x].battery) + "%")

        if messageType == "05" and frameCounter >= "2" and sensors[x].name == sensorName:
            print(sensors[x].name + " is connected")
            sensors[x].connected = True


def on_scan_message(client, userdata, msg):
    global MQTT_output
    global sensors
    # print(f"Received `{msg.payload.decode()}` ")
    theString = str(msg.payload.decode("utf-8"))
    # print(theString)
    msg_a = json.loads(theString)

    sensorName = str(msg_a['deviceName'])
    MQTT_output += "[" + sensorName + "] -" + " SNR: " + str(
        msg_a["rxInfo"][0]['loRaSNR']) + " | RSSI: " + str(msg_a["rxInfo"][0]['rssi']) + "\n"

    MQTT_output_data.append("[" + sensorName + "] -" + " SNR: " + str(
        msg_a["rxInfo"][0]['loRaSNR']) + " | RSSI: " + str(msg_a["rxInfo"][0]['rssi']) + "\n")

    print(MQTT_output)
    TempMeasRSSI.append(msg_a["rxInfo"][0]['rssi'])

    # print(sensorName + )
    TempMeasSNR.append(msg_a["rxInfo"][0]['loRaSNR'])

    ##ADD data to Array
    # print(json.Parse(msg_a["rxInfo"]));

    exists = False
    for x in range(len(sensors)):
        if sensors[x].name == sensorName:
            print("add data to object " + str(sensors[x].name))
            sensors[x].addMeasurement(msg_a["rxInfo"][0]['rssi'], msg_a["rxInfo"][0]['loRaSNR'])
            exists = True

    if not exists:
        print("added new: " + sensorName)
        new_sensor = Sensor(sensorName)
        new_sensor.addMeasurement(msg_a["rxInfo"][0]['rssi'], msg_a["rxInfo"][0]['loRaSNR'])
        sensors.append(new_sensor)


############################################ MEASUREMENT #####################################################
def MeasureRSSI():
    # global TempMeas = null
    global IsMeassuring
    global MQTT_output
    print("Measure tread started\n")
    client = connect_mqtt()
    subscribe_scan(client)
    client.loop_start()
    timeRef_start = time.perf_counter()

    print("loop will begin\n")
    MQTT_output = ""
    IsMeassuring = True
    while timeRef_start + 60.0 > time.perf_counter():
        global TimePerc
        TimePerc = time.perf_counter() - timeRef_start

    client.loop_stop()
    IsMeassuring = False
    if not TempMeasSNR or not TempMeasRSSI:
        print("> NO RESULTS <")
        return

    ### Save measurements to database ###
    # db = sqlite3.connect('data')
    # cursor = db.cursor()
    # cursor.execute("INSERT INTO data (ID, TS, RSSI, SNR) VALUES ('2', ?, ?, ?)", (
    #    datetime.datetime.now(), int(statistics.median(TempMeasRSSI)), float(statistics.median(TempMeasSNR)),))
    # db.commit()
    # db.close()

    print("----- MEASSUREMENT RESULTS --------\n")

    print("SNR Results:")
    stringSNR = ""
    for x in TempMeasSNR:
        stringSNR += str(x) + ","
    print(stringSNR)
    if len(TempMeasSNR) == 1:
        print("Mean: " + str(statistics.mean(TempMeasSNR)) + ", Median: " + str(
            statistics.median(TempMeasSNR)) + ", Var: N/A" + "\n")
    else:
        print("Mean: " + str(statistics.mean(TempMeasSNR)) + ", Median: " + str(
            statistics.median(TempMeasSNR)) + ", Var: " + str(statistics.variance(TempMeasSNR)) + "\n")

    print("RSSI Results:")
    stringRSSI = ""
    for x in TempMeasRSSI:
        stringRSSI += str(x) + ","
    print(stringRSSI)

    if len(TempMeasRSSI) == 1:
        print("Mean: " + str(statistics.mean(TempMeasRSSI)) + ", Median: " + str(
            statistics.median(TempMeasRSSI)) + ", Var: N/A" + "\n")
    else:
        print("Mean: " + str(statistics.mean(TempMeasRSSI)) + ", Median: " + str(
            statistics.median(TempMeasRSSI)) + ", Var: " + str(statistics.variance(TempMeasRSSI)) + "\n")

    print("-----------------------------------")


def MessaureBattery():
    global battery_scan_finished
    global total_devices

    client = connect_mqtt()
    subscribe_battery(client)
    client.loop_start()
    print("Messaure battery and connection status have started")
    print("Total sensors addded to ChirpStack is " + str(total_devices))
    while not battery_scan_finished:
        sensors_connected = 0
        for x in range(len(sensors)):
            if sensors[x].connected:
                sensors_connected += 1
                # print("Sensors connected are: " + str(sensors_connected))
        if sensors_connected == total_devices:
            battery_scan_finished = True
            print("We are done")

    print("Messaure battery and connection status have started")
    client.loop_stop()


############################################ BTN_CLICKED #####################################################
def start_scan():
    t0 = threading.Thread(target=MeasureRSSI)
    t0.start()


def start_MessaureBattery():
    t1 = threading.Thread(target=MessaureBattery)
    t1.start()


def configureTotalDevices():
    global total_devices
    total_devices = int(getTotalDevices())

# total_devices = int(getTotalDevices())
# start_MessaureBattery()
# while True:
#    None
