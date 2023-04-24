import Adafruit_DHT
import time

# DHT11 센서 객체를 선언한다
sensor = Adafruit_DHT.DHT11

# DHT11 센서와 연결된 핀을 정의한다
pin = 27

if __name__ == "__main__":
    
    # 센서의 정보를 1초에 한번씩 출력한다
    while(True):
        # 온습도 데이터를 센서로부터 가져온다
        humidity, temperature = Adafruit_DHT.read(sensor, pin)
        
        # 만약 온습도 데이터가 None 값이 아니라면 값을 출력한다
        if humidity is not None and temperature is not None:
            print('')
            print('Temp={}°C Humidity={}%'.format(temperature, humidity))
        else:
            print('.',end='')

        # 1초간 대기한다
        time.sleep(1.0)
