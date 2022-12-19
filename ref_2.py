import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.resizable(0, 0)
root.title('AISW계산기[2201110215]')


display_val = 0
sub_val = 0

str_value = tk.StringVar()
str_value.set(str(display_val))


num_result = tk.Entry(root, state = 'readonly', textvariable = str_value, justify = 'right', bg = 'white', fg = 'red')
num_result.grid(row = 0, column = 0, columnspan = 4, padx = 22, pady = 10, ipadx = 100, ipady = 40)


sub_str_value = tk.StringVar()
sub_str_value.set(sub_val)

num_process = tk.Entry(root, state = 'readonly', textvariable = sub_str_value, justify = 'right', bg = 'white', fg = 'red')
num_process.grid(row = 1, column = 2, columnspan = 2, ipadx = 24, ipady = 20)



root.mainloop()
