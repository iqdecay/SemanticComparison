try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()

# width is in text characters
# height is in text lines
b1 = tk.Button(root, text="Button1", width=12)
b2 = tk.Button(root, text="Button2", width=36, bg='green')
b3 = tk.Button(root, text="Button3", width=24, height=3, bg='red')

# use grid layout manager
b1.grid(row=0, column=0, sticky='w')
b2.grid(row=1, column=0, columnspan=3)
b3.grid(row=2, column=0, rowspan=3, sticky='w')

root.mainloop()