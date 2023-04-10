import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buzzer = 12

# 4옥타브 도레미~ 5옥타브 도
SCALE = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294]
Delay = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5]
if __name__ == '__main__':
    GPIO.setup(buzzer, GPIO.OUT) 
    pwm = GPIO.PWM(buzzer, 100) # 100Hz
    try:

        # pwm 시작
        pwm.start(100) 
        
        # dutycycle 50%
        pwm.ChangeDutyCycle(50) 
        for i in SCALE:
            pwm.ChangeFrequency(i) #주파수 변경          
            time.sleep(Delay[i])  #<---- 안됨!!! ㅠㅠ
        
        # Buzzer를 끈다
        pwm.ChangeDutyCycle(100) 
        print("OFF")

    # 종료 등의 키보드 인터럽트 발생시 처리 동작
    except KeyboardInterrupt:
        # Buzzer를 끈다
        GPIO.output(buzzer,GPIO.LOW)
        # GPIO를 초기화한다
        GPIO.cleanup()
