#!/usr/bin/python
import os, sys
import serial
import time

ser = serial.Serial('/dev/ttyUSB4',19200, timeout = 10)

while True:
   line = ser.readline()
   if len(line) == 0:
      print("Time out! Exit.\n")
      sys.exit()
   print line,
