# I2C 사용을 위한 모듈 smbus
import math
import smbus

# 지연시간 제어를 위해 time 모듈을 사용한다.
import time

bus = smbus.SMBus(1)   # I2C 포트 번호 (1번을 씀)
i2c_address = 0x48

# PCF8591 칩에서 데이터를 받기위한 명령어다.
command = 0x44

# try-except 는 파이썬의 예외처리 구문으로
# 키보드로 Ctrl + C를 누를시 프로그램이 종료 된다.
try:
    while(1) :
        # i2c의 주소와 명령어를 전송하여 5Byte의 데이터를 읽어온다.
        # 맨 앞의 dummy data(index 0번 데이터)를 제외하고 뒤 4Byte가 4개의 ADC 포트 데이터이다.
        adc_data = bus.read_i2c_block_data(i2c_address, command, 5)
        # I2C로 부터 센서 값을 읽어온다. 다 PSD 센서는 3번이다
        psd_value = (adc_data[4] / 255.0 * 3.3) * 3 / 2
        psd_value = 29.988 * math.pow(psd_value , -1.173)
        psd_value = round(psd_value, 2)
        print("PSD : " + str(psd_value) + " %")
        time.sleep(0.1)
    # 종료 등의 키보드 인터럽트 발생시 처리 동작
except KeyboardInterrupt:
    pass
