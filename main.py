import csv_to_pickle as csv
import text_processing
import os

#  The csv file contains texts separate by commas
csv_filename = "enter filename with .csv"
base_name = "enter pickle name without extension"

# From the pickle name, initialize all of the filenames
pickle_name = base_name + ".pkl"

# If the pickle file exists, then go directly to treatment
cwd = os.getcwd()
complete_path = "{}/{}".format(cwd, pickle_name)
if not os.path.exists(complete_path):
    print("Pickle not found under {}, treating the csv".format(complete_path))
    csv_path = "{}/{}".format(cwd, csv_filename)
    file_dictionary = csv.open_csv(csv_path)
    csv.save_csv_as_pickle(file_dictionary, pickle_name)
else:
    print("Pickle found, not treating the CSV")

""" Process text : 
 - tokenization
 - remove long and short words
 - remove punctuation and numbers
"""

# TODO : handle the choice of language, defaulting to english for now

# If the treated text exists, do not run the treatment again
treated_dictionary_pickle_name = pic
treated_dictionary =
