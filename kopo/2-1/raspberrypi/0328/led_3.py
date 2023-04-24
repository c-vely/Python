# shift 연산자로 해보기   ---> 수정중

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

shift_val = 0x01
for i in range(3):
    shift_val = shift_val << i   # <--- 수정 중

    if shift_val == 0x08:
        shift_val = 0x01
    ledOn(shift_val)
    time.sleep(1)

for i in range(3):
    shift_val = shift_val << i

    if shift_val == 0x08:
        shift_val = 0x01
    ledOff(shift_val)
    time.sleep(1)

ledOn(RED_LED)
ledOn(GREEN_LED)
ledOn(BLUE_LED)
time.sleep(1)

ledOff(RED_LED)
ledOff(GREEN_LED)
ledOff(BLUE_LED)
time.sleep(1)

