import tkinter as tk
from functools import partial
from tkinter.constants import *

import document_reading


def validate(i):
    print(i)


root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.state('zoomed')  # The "zoomed" state doesn't work on every machine
a = document_reading.load('small_pickle', '')
key_list = list(a.keys())
ticket_example = key_list[0]
ticket_compared = key_list[18]
text_example = a[ticket_example]["text"]
text_compared = a[ticket_compared]["text"]
text_zone = tk.Text(root, wrap=WORD)
text_zone.insert(INSERT, text_example)
text_zone.insert(INSERT, '\n\n\n' + text_compared)
text_zone.configure(state='disabled')

# text_zone.grid(row=0, columnspan=10)
text_zone.pack(side=TOP)

button = tk.Button(root, text="OK", command=validate)
button_values = [(str(i), i) for i in range(10)]

for text, integer in button_values:
    b = tk.Button(root, text=text, width=32, command=partial(validate, integer))
    # b.grid(row=1, column=integer)
    b.pack(side=LEFT, fill=Y)
root.mainloop()
