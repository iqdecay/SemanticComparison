import csv_to_pickle as csv
import text_processing, document_io
import os

# TODO : have the program ask for input
#  The csv file contains texts separate by commas
csv_filename = "enter filename with .csv"
base_name = "enter pickle name without extension"

# From the pickle name, initialize all of the filenames
pickle_name = base_name + ".pkl"

# If the pickle file exists, then go directly to treatment
cwd = os.getcwd()
if not os.path.exists("{}/{}".format(cwd, pickle_name)):
    print("Pickle not found under {}, treating the csv".format(complete_path))
    csv_path = "{}/{}".format(cwd, csv_filename)
    file_dictionary = csv.open_csv(csv_path)
    csv.save_csv_as_pickle(file_dictionary, pickle_name)
else:
    print("Pickle found, not treating the CSV")
    file_dictionary = document_io.load(pickle_name)

""" Process text : 
 - tokenization
 - remove long and short words
 - remove punctuation and numbers
"""

# TODO : handle the choice of language, defaulting to english for now

# If the treated text exists, do not run the treatment again
treated_dictionary_pickle_name = base_name + "_treated_dict" + ".pkl"

if not os.path.exists("{}/{}".format(cwd, treated_dictionary_pickle_name)):
    #  Specify the parameters, cf text_processing.py for explanation
    treated_dictionary = text_processing.treat_dictionary(file_dictionary, number_of_texts=1000000, min_len=1,
                                                          max_len=15
                                                          )
    document_io.save(treated_dictionary_pickle_name, treated_dictionary, cwd)
    print("The text was treated and saved under {}{}".format(cwd, treated_dictionary_pickle_name))
else:
    print("Treated text was found, not processing it")
    treated_dictionary = document_io.load(treated_dictionary_pickle_name)

