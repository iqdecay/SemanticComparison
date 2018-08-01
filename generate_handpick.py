import document_io
from random import shuffle

tickets = document_io.load("csv_file_as_pickle", '')
print(len(tickets))

keys = list(tickets.keys())
shuffle(keys)
final_sample = []
for key in keys:
    final_sample.append(key)
final_sample = final_sample[:1000]

document_io.save("1000_tickets", final_sample, "others", overwrite=True)
