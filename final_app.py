import tkinter as tk
from tkinter.constants import *  # For improved readability
from functools import partial  # Used instead of lambda functions in the buttons

import document_io

# We prepare the experiment
# The experience set is a list of dictionary. Each dictionary is under the form
#  { 'ticket_a': ticket_id,
#     'ticket_b': ticket_id,
#       'similarity': similarity }
# and possibly another field : 'user_rating', if the test has already been ran but is ran one more time
experience_list = document_io.load("aggregate_matched", "results")  # Loading the prepared experience set
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
        self.ticket_a = current_experience["ticket_a"]
        self.ticket_b = current_experience["ticket_b"]
        self.similarity = current_experience["similarity"]
        self.text_a = self.tickets[self.ticket_a]["text"]
        self.text_b = self.tickets[self.ticket_b]["text"]
        self.update_text("top")
        self.update_text("bottom")

    def update_text(self, position):
        """
        Update the text in the text widget when a pair of tickets has received user judgment
        :param position: which text (ie a or b) will be updated
        :return: None
        """
        if position == "top":
            text_widget = self.text_top
            text = self.text_a
        elif position == "bottom":
            text_widget = self.text_bottom
            text = self.text_b
        else:
            raise ValueError("position argument must be either top or bottom")

        text_widget.configure(state="normal")  # Allow the program to modify the text in the widget
        text_widget.delete(1.0, END)
        text_widget.insert(INSERT, text)
        text_widget.configure(state="disabled")  # Prevent user input in the text zone
        return None

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
        self.parent.rowconfigure(1, weight=1)
        self.parent.rowconfigure(2, weight=1)
        # Configure the top text widget
        self.text_top = tk.Text(self.parent, wrap=WORD)  # The wrap=WORD option avoids newline in the middle of words
        self.text_top.grid(row=0, column=0, columnspan=11, sticky=N + S + E + W)
        # Configure the bottom text widget
        self.text_bottom = tk.Text(self.parent, wrap=WORD)
        self.text_bottom.grid(row=1, column=0, columnspan=11, sticky=N + S + E + W)
        # Configure the buttons the user will click to mark the pairs
        button_values = [(str(i), i) for i in range(11)]
        for text, integer in button_values:
            self.parent.columnconfigure(integer, weight=1)  # Allow for proper resizing of the window
            b = tk.Button(self.parent, text=text, command=partial(self.validate, integer))
            b.grid(row=2, column=integer, columnspan=1, sticky=N + S + W + E)
        self.validate(None)


root = tk.Tk()
root.title('Test UI')
root.state('zoomed')
myapp = MyApp(root, number_tickets, experience_list, tickets_dict)
root.mainloop()
