import tkinter as tk
import tkinter.messagebox as msgbox
from typing import SupportsBytes

root = tk.Tk()
root.resizable(False, False)
root.title('계산기')

display_val = 0
oper_val = ''
sub_val = ''

str_value = tk.StringVar()
str_value.set(str(display_val))

entry = tk.Entry(root, state='readonly', textvariable=str_value, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=80, ipady=30)

sub_str_value = tk.StringVar()
sub_str_value.set(sub_val)

sub_entry = tk.Entry(root, state='readonly', textvariable=sub_str_value, justify='right')
sub_entry.grid(row=1, column=2, columnspan=2, ipadx=10, ipady=10)

num = ([1,2,3,4], [5,6,7,8], [9,'0', '+', '-'], ['/', '*', '=', 'C'])
operation = ('+', '-', '/', '*')

def click(value):
    global display_val, oper_btn, sub_val, oper_val

    try:
        str_value.set(str(display_val))
        value = int(value)
        display_val = display_val * 10 + value
        str_value.set(str(display_val))
        oper_val = ''

    except:
        if value == '=':
            if oper_val in operation:
                print(i)
                msgbox.showerror('Error', 'Operation in last. Please enter some numbers first.')
                return
            else:
                print(sub_val)
                sub_val = sub_val + str(display_val)
                print(sub_val)
                display_val = eval(sub_val)
                print(sub_val)
                str_value.set(str(display_val))
                sub_str_value.set(sub_val)
                display_val = 0
                sub_val = ''

        elif value == 'C':
            display_val = 0
            sub_val = ''
            oper_val = ''
            str_value.set(str(display_val))
            sub_str_value.set(sub_val)

        elif oper_val in operation:
            msgbos.showerrer('Error', 'Cannot insert operarion continuesly. Please insert Numbers.')
                
        else:
            sub_val = sub_val + str(display_val) + str(value)
            display_val = 0
            oper_val = value
            str_value.set(str(display_val))
            sub_str_value.set(sub_val)
for i, items in enumerate(num, start=2):
    for j, item in enumerate(items):
        btn = tk.Button(root, text=item, width=10, height=5, command=lambda cmd=item: click(cmd))
        btn.grid(column=j, row=i)

root.mainloop()














