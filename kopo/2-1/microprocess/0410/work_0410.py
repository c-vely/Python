from gpiozero import PWMLED        
from gpiozero import Button     
from time import sleep             


button = Button(3) 
pwmled = PWMLED(4)


brightness=[0, 0.25, 0.5, 0.75, 1]
cnt = 0
flag = 0


while True:
    

    if button.is_pressed:
        if flag == 0:
            flag = 1
            if -1 < cnt < 5:
                cnt += 1

            if cnt == 5:
                cnt = 0
                
        print(cnt)
        pwmled.value=brightness[cnt]  
        print(pwmled.value)                
        print("Button is pressed")          
        sleep(0.05)
        
    else:
        flag = 0
        print("Button is not pressed")       
        sleep(0.05)
