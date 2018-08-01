import document_io
from random import shuffle

tickets = document_io.load("aggregate", "experience")
print(len(tickets))

keys = list(tickets.keys())
shuffle(keys)
final_sample = []
for key in keys:
    final_sample.append(key)
final_sample = final_sample[:1000]

document_io.save("1000_tickets_fourth_batch", final_sample, "others", overwrite=True)
