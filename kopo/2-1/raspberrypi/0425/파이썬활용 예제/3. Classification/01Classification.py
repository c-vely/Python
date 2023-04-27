import tensorflow as tf
import tensorflow.keras.applications as applications

import numpy as np
import cv2
import os
import time
import threading


# 학습 모델 저장 경로
MODEL_PATH = "training_models"

MODEL_H5_PATH = os.path.join(MODEL_PATH, "classification_model.h5")
LABELS_PATH = os.path.join(MODEL_PATH, "classes.txt")


# 카메라 설정
def _reader(camera):
    global ret, frame
    
    while(True):
        ret, frame = camera.read()
        
        if(ret == False or frame is None):
            break
        time.sleep(0.001)


camera = cv2.VideoCapture('http://127.0.0.1:8090/?action=stream')

read_thread = threading.Thread(target=_reader, args=(camera,))
read_thread.daemon = True
read_thread.start()


# 모델 불러오기
model = tf.keras.models.load_model(MODEL_H5_PATH)


# 클래스 이름 가져오기
category_index = open(LABELS_PATH, 'r').read().splitlines()


# 이미지 정규화 방법을 가져옵니다.
if("mobilenet" in model.name):
    preprocessor = applications.mobilenet.preprocess_input
else:
    preprocessor = lambda x: x


print("이미지 추론 진행 중 (클래스가 처음 만들어질 때만 1번 실행)")

# 처음 추론 시 생기는 딜레이 방지
tf_input_tensor_name: np.zeros((1, 224, 224, 3))


# 이미지 분류를 진행하는 함수
def execute(frame):
    frame_cls = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_cls = cv2.resize(frame_cls, (224, 224), interpolation=cv2.INTER_AREA)
    frame_cls = preprocessor(frame_cls)

    scores = model.predict(frame_cls[None, ...])
    scores = np.squeeze(scores)
    
    top_k = scores.argsort()[-5:][::-1]
    
    result_label = category_index[top_k[0]]
    result_accuracy = scores[top_k[0]]
    
    return (result_label, result_accuracy)


try:
    while(True):
        if(not ret):
            break
        
        classes_name, scores = execute(frame)
        
        text_label = classes_name + " : " + str(round(scores * 100, 2)) + "%"

        cv2.putText(
            img = frame,
            text = text_label,
            org = (30, 40),
            fontFace = cv2.FONT_HERSHEY_SIMPLEX,
            fontScale = frame.shape[0] * 1.5e-3,
            color = (255, 0, 255),
            thickness = 2,
            lineType = cv2.LINE_AA
        )
        
        cv2.imshow('Classification', frame)
        
        waitKey = cv2.waitKey(1)

        if waitKey == ord('q'):
            break


except KeyboardInterrupt:
    pass

except Exception as e:
    import traceback
    traceback.print_exc()
    print(e)

finally:
    cv2.destroyAllWindows()
    print("종료")


camera.release()
tf.keras.backend.clear_session()
