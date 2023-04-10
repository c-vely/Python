import Adafruit_DHT
import time

# DHT11 센서 객체를 선언한다
sensor = Adafruit_DHT.DHT11

# DHT11 센서와 연결된 핀을 정의한다
pin = 27

if __name__ == "__main__":
# 무한 반복하여 센서의 정보를 1초에 한번씩 출력한다
    while(True):
        # 습도 데이터를 센서로부터 가져온다
        sensorValue = Adafruit_DHT.read(sensor, pin)
        humidity = sensorValue[0]
        
        # 만약 습도 데이터가 None 값이 아니라면 값을 출력한다
        if humidity is not None:
            print('Humidity={}%'.format(humidity))
        else:
            print('Failed to get reading. Try again!')

        # 1초간 대기한다
        time.sleep(1.0)
