# 1 > 3 > 7 > 6 > 4 > 0 > 1,3,7 > 6,4,0

import time
import smbus

RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100

state = None
bus = None

# i2c를 사용하기 위해 smbus 모듈을 초기화한다.
def ledInit():
    global state
    global bus
    state = 0b00000000
    bus = smbus.SMBus(1)
def ledOn(cmd):
    global state
    state = (state | cmd) 
    print(state)
    bus.write_byte(0x20, state) 
def ledOff(cmd):
    global state
    state = (state & (~cmd)) 
    print(state)
    bus.write_byte(0x20, state)


ledInit()

ledOn(RED_LED)
time.sleep(0.5)
ledOn(GREEN_LED)
time.sleep(0.5)
ledOn(BLUE_LED)
time.sleep(0.5)

ledOff(RED_LED)
time.sleep(0.5)
ledOff(GREEN_LED)
time.sleep(0.5)
ledOff(BLUE_LED)
time.sleep(0.5)

ledOn(RED_LED)
ledOn(GREEN_LED)
ledOn(BLUE_LED)
time.sleep(1)

ledOff(RED_LED)
ledOff(GREEN_LED)
ledOff(BLUE_LED)
time.sleep(1)

