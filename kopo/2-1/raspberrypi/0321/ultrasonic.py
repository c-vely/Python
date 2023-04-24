import RPi.GPIO as GPIO
import time

# BCM 핀맵을 사용한다
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 초음파센서에서 사용되는 핀
trig = 23
echo = 24

if __name__ == '__main__':
    # trig핀을 출력으로 설정한다
    GPIO.setup(trig, GPIO.OUT)

    # echo핀을 입력으로 설정한다
    GPIO.setup(echo, GPIO.IN)

    try :
    # 스레드는 반복하며 초음파 센서의 거리를 측정한다.
        while True :
            # 거리 측정을 위해 초음파를 쏜다
            GPIO.output(trig, False)
            time.sleep(0.5)
            GPIO.output(trig, True)
            time.sleep(0.00001)
            GPIO.output(trig, False)

            # 초음파 출력 후의 시간과 다시 받았을때의 시간을 계산한다
            while GPIO.input(echo) == 0 :
                signal_Start = time.time()
            while GPIO.input(echo) == 1 :
                signal_End = time.time()
            
            # 응답 받은 시간과 초음파의 속도 등으로 거리를 계산한다
            responseDuration = signal_End - signal_Start
            
            # (34000cm/s) 왕복이므로 2를 나누어준다
            distance = responseDuration * 34000 / 2
            
            # 소수점 둘 째 자리까지만 출력한다
            distance = round(distance, 2)
            
            # 1000cm 를 초과할시 값을 표기하지 않는다
            if distance < 1000 : 
                print("Distance : " + str(distance) + "cm")
            else:
                pass
            
    # 종료 등의 키보드 인터럽트 발생시 처리 동작
    except KeyboardInterrupt:
        # GPIO를 초기화한다
        GPIO.cleanup()
