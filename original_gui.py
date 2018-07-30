from tkinter import *
from functools import partial

import document_reading

a = document_reading.load('small_pickle', '')
key_list = list(a.keys())
ticket_example = key_list[0]
ticket_compared = key_list[18]
text_example = a[ticket_example]["text"]
text_compared = a[ticket_compared]["text"]


class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.text_top = Text(self.parent, wrap=WORD, )
        self.text_top.insert(INSERT, text_example)
        self.text_top.insert(INSERT, '\n\n\n' + text_compared)
        self.text_top.configure(state='disabled')
        self.text_top.grid(row=0, column=0, columnspan=10, sticky=N+S+E+W)

        def validate(i):
            print(i)

        button_values = [(str(i), i) for i in range(10)]
        for text, integer in button_values:
            b = Button(self.parent, text=text, command=partial(validate, integer))
            b.grid(row=1, column=integer, columnspan=1, sticky=N + S + W + E)


root = Tk()
root.title('Test UI')
root.state('zoomed')
myapp = MyApp(root)
root.mainloop()
