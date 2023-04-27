from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# 모델 불러오기
model = load_model('keras_model.h5')

# keras 모델에 입력할 올바른 모양의 배열을 만듭니다.
# 배열에 넣을 수 있는 '길이' 또는 이미지 수는
# 모양 튜플의 첫 번째 위치에 의해 결정됩니다(이 경우 1).
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# 이것을 이미지 경로로 바꿉니다.
image = Image.open('paper.jpg')

# TM2에서와 동일한 전략으로 이미지를 224x224로 크기 조정:
# 이미지 크기를 224x224 이상으로 조정한 다음 중앙에서 자르기
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#이미지를 numpy 배열로 변환
image_array = np.asarray(image)

# 이미지 정규화
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# 이미지를 배열에 로드
data[0] = normalized_image_array

# 추론 실행
prediction = model.predict(data)
print(prediction)
