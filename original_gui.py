from tkinter import *
from functools import partial

import document_io

a = document_io.load('small_pickle', '')
key_list = list(a.keys())
ticket_example = key_list[0]
ticket_compared = key_list[18]
text_example = a[ticket_example]["text"]
text_compared = a[ticket_compared]["text"]


class MyApp:
    def __init__(self, parent):
        self.parent = parent
        # We give all the rows the same non-zero weight so they scale with the window
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=1)  # We add an empty row for design purposes
        self.parent.rowconfigure(2, weight=1)
        self.text_top = Text(self.parent, wrap=WORD)  # The wrap=WORD option avoids newline in the middle of words
        self.text_top.insert(INSERT, text_example)
        self.text_top.insert(INSERT, "\n==========================================================================")
        self.text_top.insert(INSERT, '\n' + text_compared)
        self.text_top.configure(state='disabled')
        self.text_top.grid(row=0, column=0, columnspan=10, sticky=N + S + E + W)

        def validate(i):
            print(i)

        button_values = [(str(i), i) for i in range(10)]
        for text, integer in button_values:
            b = Button(self.parent, text=text, command=partial(validate, integer))
            self.parent.columnconfigure(integer, weight=1)
            b.grid(row=2, column=integer, columnspan=1, sticky=N + S + W + E)


root = Tk()
root.title('Test UI')
root.state('zoomed')
myapp = MyApp(root)
root.mainloop()
