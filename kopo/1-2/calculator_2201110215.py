import tkinter as tk
import tkinter.messagebox as msgbox

# 제목
window = tk.Tk()
window.resizable(0, 0)
window.title('AISW계산기[2201110215]')


# 출력창 1, 2
num_result = tk.Entry(window, width = 50, justify = 'right', bg = 'white', fg = 'red')
num_result.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 0, ipadx = 0, ipady = 40)

num_process = tk.Entry(window, justify = 'right', bg = 'white', fg = 'red')
num_process.grid(row = 1, column = 2, columnspan = 2, padx = 0, pady = 0, ipadx = 20, ipady = 20)


# 계산
dispaly_value = 0
str_value = tk.StringVar()
str_value.set(str(dispaly_value))

sub_value = ''
subStr_value = tk.StringVar()
subStr_value.set(sub_value)
                            




window.mainloop()
