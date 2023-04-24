from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import time
import threading
import cv2
import random

value= None

def show_frame():
    ret, frame = cap.read()
    processImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processImage = cv2.resize(processImage, (640, 480))
    processImage = Image.fromarray(processImage)
    processImage = ImageTk.PhotoImage(image=processImage)
    lmain.processImage = processImage
    lmain.configure(image=processImage)
    lmain.after(1, show_frame) 

try:
    root = Tk()         
    root.title('Camera')
    root.geometry("640x520+10+10")

    lmain = Label(root)
    lmain.pack()

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("http://raspberryAI:8090/?action=stream")
    
    show_frame()
    root.mainloop()           
except KeyboardInterrupt:
    sys.exit()