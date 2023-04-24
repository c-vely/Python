from subus import SMBus
from time import sleep

bus = SMBus(1)
add = 0x48

pwmled = PWMLED(22)
brightness = 0


def readAD():
    analog = bus.read_byte(add)
    return analog

while(1):
    bus.write_byte(add, 0x03)
    sleep(0.01)
    readAD()
    an3 = readAD()
    brightness = an3 * 0.0039  # 1/256 = 0.0039
    pwdled.value = brightnes
    sleep(0.05)

    print('brightness = %3d %3f' % (an3, brightness))


