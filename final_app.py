import tkinter as tk
from tkinter.constants import *
from functools import partial  # Used instead of lambda functions in the buttons

import document_io
from main_document_similarity import experience_name
# We prepare the experiment
# The experience set is a list of dictionary. Each dictionary is under the form
#  { 'ticket_a': ticket_id,
#     'ticket_b': ticket_id,
#       'similarity': similarity }
# and possibly another field : 'user_rating', if the test has already been ran but is ran one more time
experience_list = document_io.load("handpicked", "others")  # Loading the prepared experience set
number_tickets = len(experience_list)
tickets_dict = document_io.load("csv_file_as_pickle", "")


class MyApp:

    def validate(self, i):
        result = {
            "ticket_a": self.ticket_a,
            "ticket_b": self.ticket_b,
            "similarity": self.similarity,
            "user_rating": i,
        }
        if i is not None:
            self.results.append(result)
        self.current_ticket_couple += 1
        if self.current_ticket_couple == self.number_of_tickets:
            for result in self.results:
                print(result)
            document_io.save("user_results", self.results, "results", overwrite=True)

            self.parent.destroy()
            return None
        current = self.current_ticket_couple
        current_experience = self.experiences[current]
        self.ticket_a = current_experience['ticket_a']
        self.ticket_b = current_experience['ticket_b']
        self.similarity = current_experience['similarity']
        self.text_a = self.tickets[self.ticket_a]["text"]
        self.text_b = self.tickets[self.ticket_b]["text"]
        self.update_text()

    def update_text(self):
        self.text_top.configure(state='normal')
        self.text_top.delete(1.0, END)
        self.text_top.insert(INSERT, self.text_a)
        self.text_top.insert(INSERT, "\n==========================================================================")
        self.text_top.insert(INSERT, '\n' + self.text_b)
        self.text_top.configure(state='disabled')  # Prevent user input in the text zone

    def __init__(self, parent, number_of_tickets, experiences, tickets):
        self.results = []
        self.parent = parent
        self.experiences = experiences
        self.tickets = tickets
        self.number_of_tickets = number_of_tickets
        self.current_ticket_couple = -1
        self.ticket_a = None
        self.ticket_b = None
        self.similarity = None
        self.text_a = None
        self.text_b = None
        # We give all the rows the same non-zero weight so that they scale with the window
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=1)  # We add an empty row for design purposes
        self.parent.rowconfigure(2, weight=1)
        self.text_top = tk.Text(self.parent, wrap=WORD)  # The wrap=WORD option avoids newline in the middle of words
        self.text_top.grid(row=0, column=0, columnspan=11, sticky=N + S + E + W)
        button_values = [(str(i), i) for i in range(11)]
        for text, integer in button_values:
            b = tk.Button(self.parent, text=text, command=partial(self.validate, integer))
            self.parent.columnconfigure(integer, weight=1)
            b.grid(row=2, column=integer, columnspan=1, sticky=N + S + W + E)
        self.validate(None)


root = tk.Tk()
root.title('Test UI')
root.state('zoomed')
myapp = MyApp(root, number_tickets, experience_list, tickets_dict)
root.mainloop()
