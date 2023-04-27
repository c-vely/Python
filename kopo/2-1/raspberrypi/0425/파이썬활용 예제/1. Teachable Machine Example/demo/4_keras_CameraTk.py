import PyCamera
import cv2
from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import time
import numpy as np
from PIL import Image, ImageOps
import threading
from tensorflow.keras.models import load_model

# camera = PyCamera.URLCamera("http://raspberryAI:8090/?action=stream")
camera = PyCamera.USBCamera(0)

keras_model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
img_size = (224, 224)

def readLabels():
    try:
        f = open("labels.txt", 'r')
        list_labels = []
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

def show_Frame():
    if camera.get_frame() is None:
        print('There are no more images')
    else:
        frame = camera.get_frame()
        src = cv2.flip(frame, 1)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        src = Image.fromarray(src)
        src = ImageTk.PhotoImage(image=src)
        lbl_video.src = src
        lbl_video.configure(image=src)

    lbl_video.after(1, show_Frame) 

def recogFunction():
    imglabel = readLabels()
    while True:
        if camera.get_frame() is None:
            print('There are no more images')
        else:
            frame = camera.get_frame()
            recog = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            recog = cv2.resize(recog, img_size)
            recog = Image.fromarray(recog)
            recog = ImageOps.fit(recog, img_size, Image.ANTIALIAS)
            image_array = np.asarray(recog)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized_image_array
            prediction = keras_model.predict(data)
            obj = []
            for i in prediction[0]:
                v = int(float(i)*1000)/10
                obj.append(v)
            strval_recog.set(imglabel[int(obj.index(max(obj)))] + " " + str(max(obj)) + " %")

        time.sleep(0.1)

try:
    root = Tk() 
    root.title('Camera')
    root.geometry("640x520+10+10")

    lbl_video = Label(root)
    lbl_video.pack()

    strval_recog = StringVar()
    strval_recog.set("모델 로딩 중...")
    lbl_recog = Label(root,background="yellow", textvariable = strval_recog)
    lbl_recog.pack()

    show_Frame()

    recogThread = threading.Thread(target=recogFunction)
    recogThread.setDaemon(True)
    recogThread.start()

    root.mainloop() 

except KeyboardInterrupt:
    printd("Program force quit")
    
sys.exit()
