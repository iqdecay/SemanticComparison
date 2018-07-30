from tkinter import *
from functools import partial

import document_reading

a = document_reading.load('small_pickle', '')
key_list = list(a.keys())
ticket_example = key_list[0]
ticket_compared = key_list[18]
text_example = a[ticket_example]["text"]
text_compared = a[ticket_compared]["text"]


def validate(i):
    print(i)


class MyApp():
    def __init__(self, parent):
        self.main_container = Frame(parent, background='bisque')
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.top_frame = Frame(self.main_container, background="green")
        self.bottom_frame = Frame(self.main_container, background="yellow")
        self.top_frame.pack(side="top", fill="x", expand=True)
        self.bottom_frame.pack(side="bottom", fill="x", expand=True)
        #
        # self.bottom_left = Frame(self.bottom_frame, background="pink")
        # self.bottom_right = Frame(self.bottom_frame, background="blue")
        # self.bottom_left.pack(side="left", fill="x", expand=True)
        # self.bottom_right.pack(side="right", fill="x", expand=True)

        self.text_top = Text(self.top_frame, wrap=WORD)
        self.button_top = Button(self.top_frame, text="Bonjour")
        self.text_top.insert(INSERT, text_example)
        self.text_top.insert(INSERT, '\n\n\n' + text_compared)
        self.text_top.configure(state='disabled')
        self.text_top.pack(fill='x', side=TOP)
        self.button_top.pack()
        #
        # self.text_bottom = Text(self.bottom_right, wrap=WORD)
        # self.text_bottom.insert(INSERT, text_example)
        # self.text_bottom.insert(INSERT, '\n\n\n' + text_compared)
        # self.text_bottom.configure(state='disabled')
        # self.text_bottom.pack(fill='x', side=TOP)

        button_values = [(str(i), i) for i in range(10)]
        for text, integer in button_values:
            b = Button(self.bottom_frame, text=text, command=partial(validate, integer))
            b.grid(row=0, column=integer, sticky=N+S+W+E)


root = Tk()
root.title('Test UI')
myapp = MyApp(root)
root.state('zoomed')
root.mainloop()
