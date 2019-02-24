import csv_to_pickle as csv
import os

#  The csv file contains texts separate by commas
filename = "enter the csv filename here"

pickle_name = "enter the pickle name here"
if pickle_name[-4:] != ".pkl":
    pickle_name = pickle_name + ".pkl"

# If the pickle file exists, then go directly to treatment
cwd = os.getcwd()
complete_path = "{}/{}".format(cwd, pickle_name)
if not os.path.exists(complete_path):
    print("Pickle not found under {}, treating the csv".format(complete_path))
    file_dictionary = csv.open_csv(complete_path)
    csv.save_csv_as_pickle(file_dictionary, pickle_name)
else:
    print("Pickle found, not treating the CSV")




