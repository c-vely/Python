import tensorflow as tf
from scripts import detection_color

import numpy as np
import cv2
import os
import time
import threading


# 학습 모델 저장 경로
MODEL_PATH = "training_models"
CLASS_FILE_PATH = "classes.txt"

MODEL_FILE_PATH = os.path.join(MODEL_PATH, "saved_model")


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
model = tf.compat.v2.saved_model.load(MODEL_FILE_PATH, tags=[tf.compat.v2.saved_model.SERVING])


# 클래스 이름 가져오기
category_index = open(CLASS_FILE_PATH, 'r').read().splitlines()

color_list = detection_color.ColorList
color_list = [color_list[(i - 1) % len(color_list)]['code'] for i in range(len(color_list))]


print("추론 진행 중 (클래스가 처음 만들어질 때만 1번 실행)")

# 처음 추론 시 딜레이 방지
tf_input_tensor_name : np.zeros((1, 300, 300, 3))


# 객체 감지를 진행하는 함수
def execute(frame):
    frame_det = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_det = cv2.resize(frame_det, (300, 300), interpolation=cv2.INTER_AREA)

    try:
        output_dict = model(frame_det[None, ...])
        scores = output_dict["detection_scores"][0].numpy()
        boxes = output_dict["detection_boxes"][0].numpy()
        classes = output_dict["detection_classes"][0].numpy().astype(int)
        
    except (tf.errors.UnknownError, tf.errors.ResourceExhaustedError, tf.errors.InternalError) as e:
        print(e)
        print("GPU 메모리 부족 혹은 다른 원인으로 인해 작업이 중단되었습니다.")
        return

    class_names = np.array([category_index[cls_num-1] for cls_num in classes])
    draw_colors = np.array([color_list[cls_num-1] for cls_num in classes])

    percentage = 0.5
    mask = np.where(scores >= percentage)[0]
    scores = scores[mask]
    boxes = boxes[mask]
    classes = classes[mask]
    class_names = class_names[mask]
    draw_colors = draw_colors[mask]
    num_detections = len(mask)

    return (scores, boxes, classes, class_names, draw_colors, num_detections)


# Hex 코드를 RGB 값으로 변환하는 함수
def hexToRGB(hex_code):
    h = hex_code.lstrip('#')
    
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


try:
    while(True):
        original_frame = frame.copy()
        
        if(not ret):
            break
            
        scores, boxes, classes, class_names, draw_colors, num_detections = execute(frame)
        
        box = boxes * np.array([frame.shape[0], frame.shape[1], frame.shape[0], frame.shape[1]])
        box = np.round(box).astype(int)

        fontScale = frame.shape[0] * 1.3e-3
        topFontScale = frame.shape[0] * 1.5e-3
        
        for i in range(num_detections):
            (y1, x1, y2, x2) = box[i]
            boxW = x2 - x1
            boxH = y2 - y1
            
            rgb_color = hexToRGB(draw_colors[i])
            bgr_color = rgb_color[::-1]
        
            cv2.rectangle(
                img = frame,
                pt1 = (x1, y1),
                pt2 = (x2, y2),
                color = bgr_color,
                thickness = 4,
            )
        
            text_label = "{0}:{1:.1%}".format(class_names[i], scores[i])
            
            x, y = (int(x1 + 3), int(y1 + 13)) if True else (int(x1), int(y1))

            size = cv2.getTextSize(text_label, cv2.FONT_HERSHEY_SIMPLEX, fontScale, 4)[0]

            cv2.rectangle(
                img = frame,
                pt1 = (x, y - size[1]),
                pt2 = (x + size[0], y),
                color = bgr_color,
                thickness = cv2.FILLED
            )
            
            cv2.putText(
                img = frame,
                text = text_label,
                org = (x, y),
                fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                fontScale = fontScale,
                color = (0, 0, 0),
                thickness = 2
            )
        
        frame = cv2.addWeighted(original_frame, 0.4, frame, 1 - 0.4, 0)
        
        cv2.imshow('Object Detection', frame)
        
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
