from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import PyCamera
import cv2
from PIL import Image, ImageOps
import time

# camera = PyCamera.URLCamera("http://raspberryAI:8090/?action=stream")
camera = PyCamera.USBCamera(0)

def readLabels():
    f = open("labels.txt", 'r')
    list_labels = []
    try:
        while True:
            line = f.readline()
            if not line: break
            getlabel = line.split(' ')
            getlabel = getlabel[1].split('\n')
            list_labels.append(getlabel[0])
        f.close()
    except Exception as e :
        print(e)
    return list_labels

# 모델 불러오기
keras_model = load_model('keras_model.h5')

# keras 모델에 입력할 올바른 모양의 배열을 만듭니다.
# 배열에 넣을 수 있는 '길이' 또는 이미지 수는
# 모양 튜플의 첫 번째 위치에 의해 결정됩니다(이 경우 1).
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
    if(camera.get_frame() is None):
        print('There are no more images')
    else:
        # 이미지 대신 카메라에서 한 프레임을 가져온다.
        image = camera.get_frame()

        # TM2에서와 동일한 전략으로 이미지를 224x224로 크기 조정:
        # 이미지 크기를 224x224 이상으로 조정한 다음 중앙에서 자르기
        img_size = (224, 224)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, img_size)
        image = Image.fromarray(image)

        image = ImageOps.fit(image, img_size, Image.ANTIALIAS)

        #이미지를 numpy 배열로 변환
        image_array = np.asarray(image)

        # 이미지 정규화
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # 이미지를 배열에 로드
        data[0] = normalized_image_array

        # 추론 실행
        prediction = keras_model.predict(data)
        obj = []
        for i in prediction[0]:
            v = int(float(i)*1000)/10
            obj.append(v)
        label_idx = int(obj.index(max(obj)))
        label_pred_rate = max(obj)

        list_labels = readLabels()

        print("label:{} / pred_rate:{}%".format(list_labels[label_idx], label_pred_rate))
        
        time.sleep(0.1)
    
