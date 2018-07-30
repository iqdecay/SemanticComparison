import os
import datetime

import document_reading
import csv_to_pickle


save_name = "save_01"
if __name__ == "__main__":
    csv_pickle_name = csv_to_pickle.csv_pickle_name
    if not os.path.exists("obj/{}.pkl".format(csv_pickle_name)):
        raise FileNotFoundError("The file obj/{} doesn't exist, please run csv_to_pickle.py".format(csv_pickle_name))
    csv_file_under_dict_form = document_reading.load(csv_pickle_name, '')
    # Create the treatment function, via a serie of True or False parts
    # tokenize = True  # Tokenize the text, should always be True
    lemmatize = False  # Lemmatize the text, very performance-heavy.  Will use later if needed
    # clean_char = True  # Remove punctuation, numbers, and remove capitalization, should always be True
    # remove_length = True  # Remove words that are too long or too short
    # remove_stopwords = True  # Remove stopwords based on a list
    number_of_lines = 1000000
    file_with_text_treated = document_reading.treat_text(csv_file_under_dict_form, number_of_lines)

    # Create the text corpus

    document_reading.save(save_name, file_with_text_treated, 'text_processed')
