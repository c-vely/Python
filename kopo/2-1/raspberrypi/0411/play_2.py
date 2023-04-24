# 버튼 1번 녹음 + 버튼 3번 재생 + 버튼 4번 정지

import sounddevice as sd
import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import pygame
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
SW1_PIN = 4
SW3_PIN = 18
SW4_PIN = 22
SW_PIN_LIST = [SW1_PIN, SW3_PIN, SW4_PIN]
GPIO.setup(SW_PIN_LIST, GPIO.IN)

fileNamePath = 'output.wav'
sample_rate = 44100 # 샘플레이트
seconds = 5 # 녹음시간
print("{}초 동안 녹음을 준비가 끝났습니다.".format(seconds))

try:
    while(True):
        button_state = []
        for i in SW_PIN_LIST:
            button_state.append(GPIO.input(i))

        if button_state[0] == 0:
            print("{}초 동안 녹음합니다.".format(seconds))
            myrecording = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=2)
            sd.wait() # 녹음이 끝날때까지 대기
            sio.wavfile.write(fileNamePath, sample_rate, myrecording) # wav파일로 저장
            print("녹음이 끝났습니다.")
            
        elif button_state[1] == 0:
            print("재생시간 계산 중입니다.")
            samplerate, data = sio.wavfile.read(fileNamePath)
            times = data.shape[0]/samplerate

            # 반올림및 형변환을 통해 정수형태로 구한다.
            play_time = int(round(times))
            print("재생시간은 {}초 입니다.".format(play_time))

            # 재생을 위한 pygame 초기화
            pygame.mixer.init()

            # 경로를 지정하여 객체를 생성하고 재생한다.
            p = pygame.mixer.Sound(fileNamePath)
            p.play()
        elif button_state[2] == 0:
            p.stop
finally:
    GPIO.cleanup()

            




