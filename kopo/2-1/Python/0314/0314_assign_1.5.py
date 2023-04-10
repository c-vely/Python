# OKAY ---> 완성!!!!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MOTOR_P = 19
MOTOR_M = 13

SW1_PIN = 4
SW3_PIN = 18
SW4_PIN = 22

cur_state = 0
pre_state = 0


if __name__ == "__main__":
    GPIO.setup(MOTOR_P, GPIO.OUT)
    GPIO.setup(MOTOR_M, GPIO.OUT)

    GPIO.setup(SW1_PIN, GPIO.IN)
    GPIO.setup(SW3_PIN, GPIO.IN)
    GPIO.setup(SW4_PIN, GPIO.IN)
    
    try:
        while(True):
            pre_state = cur_state
                           
            print("SW1_PIN State : ", GPIO.input(SW1_PIN))
            print("SW3_PIN State : ", GPIO.input(SW3_PIN))
            print("SW4_PIN State : ", GPIO.input(SW4_PIN))
            print("cur_state : ", cur_state)
            print("pre_state : ", pre_state)
            # 0.5초간 대기한다.
            time.sleep(0.5)
            
            
            if GPIO.input(SW1_PIN)==0:
                cur_state = 1
            elif GPIO.input(SW3_PIN)==0:
                cur_state = 2
            elif GPIO.input(SW4_PIN)==0:
                cur_state = 0
            else:
                cur_state = cur_state
            
            
            if cur_state == 1:
                if pre_state == 2:
                    GPIO.output(MOTOR_P, GPIO.LOW)
                    GPIO.output(MOTOR_M, GPIO.LOW)
                    print("Stop")
                    time.sleep(0.5)
                GPIO.output(MOTOR_P, GPIO.HIGH)
                GPIO.output(MOTOR_M, GPIO.LOW)
                print("Clock Wise")
                time.sleep(0.5)
            elif cur_state == 2:
                if pre_state == 1:
                    GPIO.output(MOTOR_P, GPIO.LOW)
                    GPIO.output(MOTOR_M, GPIO.LOW)
                    print("Stop")
                    time.sleep(0.5)
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.HIGH)
                print("Reversed Clock Wise")
                time.sleep(0.5)
            elif cur_state == 0:
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.LOW)
                print("Stop")
                time.sleep(0.5)
 
                
    except KeyboardInterrupt:
        GPIO.cleanup()
        
