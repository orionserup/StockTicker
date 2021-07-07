# Boot.py Initialization Script for the project

from network import *
from machine import UART
from robin_stocks import robinhood

class ESP8266:

    # Wifi Connection Credentials
    WIFISSID = "Default SSID"
    WIFIPASS = "Default PASS"

    # Robinhood Credentials
    RHUSER = "Default RH Username"
    RHPASS = "Default PH Password"

    # Hardware Module handlers
    WLAN = None
    UART = None

    def InitWifi(self, SSID=WIFISSID, PASS=WIFIPASS):
        
        self.WIFISSID = SSID
        self.WIFIPASS = PASS
        self.WLAN = network.WLAN(network.STA_IF)
        self.WLAN.active(True)
        self.WLAN.scan()
        self.WLAN.connect(SSID, PASS)

        while not self.WLAN.isconnected():
            self.WLAN.connect(input("WI-FI SSID"), input("WI-FI Password")
        
    def InitSerial(self, PORT=1, SPEED=9600):

        self.UART = machine.UART(PORT, baudrate=SPEED)


    def __init__():
        InitWifi()
        InitSerial()

if __name__ == "__main__":
    esp = ESP8266()
