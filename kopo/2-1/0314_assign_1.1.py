# --> 정방향으로만 돌다 멈춤. 무한 반복

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MOTOR_P = 19
MOTOR_M = 13

SW1_PIN = 4
#SW2_PIN = 17
SW3_PIN = 18
SW4_PIN = 22

SW_PIN_LIST = [SW1_PIN, SW3_PIN, SW4_PIN]


if __name__ == "__main__":
    GPIO.setup(MOTOR_P, GPIO.OUT)
    GPIO.setup(MOTOR_M, GPIO.OUT)

    GPIO.setup(SW_PIN_LIST, GPIO.IN)
    
    try:
        while(True):
            GPIO.output(MOTOR_P, GPIO.LOW)
            GPIO.output(MOTOR_M, GPIO.LOW)
            print("Stop")
            
            button_state = []
            for i in SW_PIN_LIST:
                button_state.append(GPIO.input(i))
            print("Button State : ", button_state)
            # 0.5초간 대기한다.
            time.sleep(0.5)
            
            if GPIO.input(SW_PIN_LIST[0]):
                GPIO.output(MOTOR_P, GPIO.HIGH)
                GPIO.output(MOTOR_M, GPIO.LOW)
                print("Clock Wise")
                time.sleep(1)
            elif GPIO.input(SW_PIN_LIST[1]):
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.HIGH)
                print("Reversed Clock Wise")
                time.sleep(1)
            else:               
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.LOW)
                print("Stop")
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
