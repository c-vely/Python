from subus import SMBus
from time import sleep

bus = SMBus(1)
add = 0x48

def readAD():
    analog = bus.read_byte(add)
    return analog

while(1):
    bus.write_byte(add, 0x00)
    sleep(0.01)
    readAD()
    an0 = readAD()

    bus.write_byte(add, 0x01)
    sleep(0.01)
    readAD()
    an1 = readAD()

    bus.write_byte(add, 0x02)
    sleep(0.01)
    readAD()
    an2 = readAD()

    bus.write_byte(add, 0x03)
    sleep(0.01)
    readAD()
    an3 = readAD()


    print('value = %3d, %3d, %3d, %3d' % (an0, an1, an2, an3))
