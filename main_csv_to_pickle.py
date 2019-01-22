# Take the path to a csv file containing text as input, and a save it under pickle form under
# the provided name

import tqdm
import document_io


def open_csv(filepath):
    """
    Open a csv file that uses ; as separators, and return a dictionary
    The text does not undergo cleaning
    As the CSV file is supposed to be processed only once, all the lines are treated.
    The text is stored under string form.
    """
    id = 0
    file_dictionary = dict()
    csv_file = open(filepath, encoding="ISO-8859-1")
    for csv_line in tqdm.tqdm(csv_file):
        id += 1
        line = str(csv_line)
        file_dictionary[id] = line
        print(line)
    print("The CSV {} was processed".format(filepath))
    return file_dictionary


def save_csv_as_pickle(file_dict, filename):
    """Save the dictionary under pickle form"""
    document_io.save(filename, file_dict, '', overwrite=True)


if __name__ == '__main__':
    filepath = input("enter path to csv file containing text :\n")
    dictionary_file = open_csv(filepath)
    pickle_name = input("enter name for the pickle object :\n")
    save_csv_as_pickle(dictionary_file, pickle_name)
