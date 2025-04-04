# GPS module sample integration

import serial

def read_gps():
    port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
    while True:
        data = port.readline()
        if data.startswith(b"$GPGGA"):
            print("GPS Raw:", data)

read_gps()
