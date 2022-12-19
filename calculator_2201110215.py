import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.resizable(0, 0)
root.title('AISW계산기[2201110215]')



num_result = tk.Entry(root, width = 50, justify = 'right', bg = 'white', fg = 'red')
num_result.grid(row = 0, column = 0, columnspan = 1, padx = 22, pady = 10, ipadx = 0, ipady = 40)

num_process = tk.Entry(root, justify = 'right', bg = 'white', fg = 'red')
num_process.grid(row = 1, column = 2, columnspan = 2, ipadx = 0, ipady = 20)




root.mainloop()
