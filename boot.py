# Boot.py Initialization Script for the project

from network import WLAN, STA_IF
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

    # Connects to the Wifi
    def InitWifi(self, SSID=WIFISSID, PASS=WIFIPASS):
        
        self.WIFISSID = SSID
        self.WIFIPASS = PASS
        self.WLAN = WLAN(STA_IF)
        self.WLAN.active(True)
        self.WLAN.scan()
        self.WLAN.connect(SSID, PASS)

        while not self.WLAN.isconnected():
            self.WLAN.connect(input("WI-FI SSID: "), input("WI-FI Password: ")
        
    # Intializes The UART and gets it ready to send
    def InitSerial(self, PORT=1, SPEED=9600):
        self.UART = UART(PORT, baudrate=SPEED)

    # Sends a string over UART
    def SendSerial(self, string):
        if self.UART is not None:
            self.UART.write((str)string)

    # When An Object is Created Initialize the Wifi and Serial
    def __init__():
        InitWifi()
        InitSerial()

# If running this as a module, create an object and initialize everything
if __name__ == "__main__":
    esp = ESP8266()
