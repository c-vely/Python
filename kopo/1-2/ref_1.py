#tkinter 이용하기 위한 import
from tkinter import *
from tkinter import messagebox

#update_xxx를 호출하면 update함수에 매개변수 xxx 전달
def update_add():
    update("add")     
def update_subtract():
    update("subtract")
def update_reset():
    update("reset")

#초기화하고 창 만들기
window = Tk()

#누적 합 저장하는 변수
total = 0

#Label 붙이기 (누적 합 출력)
sum = Label(window);

#격자 배치 관리자 이용해서 Label 위치 정하기
sum.grid(row=0, column=1, columnspan=2)

#현재 합계: 라고 나타내는 Label
label = Label(window, text="현재 합계:")
label.grid(row=0, column=0)

#값 입력받는 창
entry = Entry(window)
entry.grid(row=1, column=0, columnspan=3)

#버튼 생성, 더하기 빼기 초기화, command를 통해 버튼 누르면 해당 함수 호출
add_button = Button(window, text="더하기(+)", command=update_add)
sub_button = Button(window, text="빼기(-)", command=update_subtract)
reset_button = Button(window, text="초기화", command=update_reset)

add_button.grid(row=2, column=0)
sub_button.grid(row=2, column=1)
reset_button.grid(row=2, column=2)

#update함수, 누적 합 계산시 이용
#entry에서 값을 받아서 total이라는 변수에 저장
def update(method):
    global total
    try:
        if method == "add":
            total += int(entry.get())
        elif method == "subtract":
            total -= int(entry.get())
        else: 
            total = 0
    #예외의 상황시 경고 메세지 박스를 띄움
    except Exception as e:
        messagebox.showerror(title='calc',message=e)
    
    #누적 합을 나타내는 label의 text를 바꿔줌
    sum.config(text=str(total))
    
    #값 입력하고 entry를 깨끗하게 비워줌
    # (새로운 입력값을 받기 위해)
    entry.delete(0, END)
    
window.mainloop()
