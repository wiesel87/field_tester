# Notes
# https://stackoverflow.com/questions/45746312/one-liner-to-remove-duplicates-keep-ordering-of-list
# https://gist.github.com/truh/de723a3bc0f837f75d3673ddf101e108
import os
import subprocess
import GUI


# interface = 'wlan0'
# name = 'sani guest'
# password = 'Mikkel2021'
# os.system('iwconfig ' + interface + ' essid ' + name + ' key ' + password)
# os.system('iwlist ' + interface + ' scan')

# os.system('nmcli device wifi')
# data = os.system('nmcli -f SSID device wifi | grep -vw SSID')
# print(data)
# os.system('nmcli device wifi connect ' + SSID + ' password ' + wifipassword)
# data = os.popen('nmcli -f SSID,SIGNAL device wifi | grep -vw SSID').read
# for line in data:
# print data

class WiFiAP:
    def __init__(self, SSID, Signal):
        self.SSID = SSID
        self.Signal = Signal


# cmd contains shell command to scan wifi and return thr give ssid list with signal strength
cmd = 'nmcli -t -f SSID,SIGNAL device wifi | grep -vw SSID'


def wifi_scan():
    process = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # The output from your shell command
    print("Wifi Scanning..")
    seen = set()

    data = []
    result = process.stdout.readline().decode()
    while 0 < len(result):
        if len(result.strip().split(':')[0]) > 0:
            if result.strip().split(':')[0] not in seen:
                data.append(WiFiAP(result.strip().split(':')[0], result.strip().split(':')[1]))
                seen.add(result.strip().split(':')[0])
        result = process.stdout.readline().decode()

    return data


def wifi_connect(SSID, wifipassword):
    print("Connecting to " + SSID + "..")
    cmd_connect = 'nmcli -w 10 device wifi connect \'' + str(SSID) + '\' password \'' + str(wifipassword) + '\''

    try:
        subprocess.check_output(cmd_connect, shell=True, stdin=None, stderr=subprocess.PIPE)
        print("Connected!")
        return 0
    except subprocess.CalledProcessError as e:
        print("Could not connect!")
        print(e.stderr)
        print("--------------")
        return -1

    # sudo kill -9 $(pidof nm-applet)


def wifi_test(SSID):
    print("Connecting to " + str(SSID) + "..")

############## WiFi #################

WIFI_BTNS = []

arrayWifi = []
arrayWifi = wifi_scan()

for x in arrayWifi:
    BTN_WIFI_SSID = GUI.Button(GUI.settings_Canvas_1,
                           # image = img0,
                           text=x.SSID, font=("SofiaProMedium", int(20.0)),
                           borderwidth=0,
                           highlightthickness=0,
                           command=lambda name=x.SSID: wifi_test(name),
                           # https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-a-for-loop-with-lambda
                           relief="flat")
    WIFI_BTNS.append(BTN_WIFI_SSID)

index = 0

for BTN in WIFI_BTNS:
    BTN.pack()

for BTN in WIFI_BTNS:
    BTN.place(
        x=20, y=50 + index * 80,
        width=332,
        height=50)
    index += 1
