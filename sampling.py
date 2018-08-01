import os

import document_io
import csv_to_pickle
import text_processing


save_name = "samples_01"
path_name = "others"
if __name__ == "__main__":
    csv_pickle_name = csv_to_pickle.csv_pickle_name
    if not os.path.exists("obj/{}.pkl".format(csv_pickle_name)):
        raise FileNotFoundError("The file obj/{} doesn't exist, please run csv_to_pickle.py".format(csv_pickle_name))
    csv_file_under_dict_form = document_io.load(csv_pickle_name, '')
    # Create the treatment function, via a serie of True or False parts
    # tokenize = True  # Tokenize the text, should always be True
    lemmatize = False  # Lemmatize the text, very performance-heavy.  Will use later if needed
    # clean_char = True  # Remove punctuation, numbers, and remove capitalization, should always be True
    # remove_length = True  # Remove words that are too long or too short
    # remove_stopwords = True  # Remove stopwords based on a list
    number_of_lines = 1000000
    file_with_text_treated = text_processing.treat_text(csv_file_under_dict_form, number_of_lines)



    # Create the text corpus

    document_io.save(save_name, file_with_text_treated, path_name)
