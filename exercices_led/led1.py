#!/usr/bin/env python


from I2C_comm import *
import time

# Allume les LEDs une à une
for i in range(4):
    led(i,True)
    time.sleep(1)
# Eteint toutes les LEDs "simultanément"
for i in range(4):
    led(i,False)
