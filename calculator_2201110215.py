import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.resizable(False, False)
root.title('2201110215')



display_val = 0
suv_val = ''

str_value = tk.StringVar()
str_value.set(str(display_val))

entry = tk.Entry(root, state = 'readonly', textvariable = str_value, justiry = 'right')
entry.grid(row = 0, column = 0; columnspan = 4, ipadx = 80, ipady = 30)





root.mainloop()
