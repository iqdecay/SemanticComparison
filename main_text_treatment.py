import os

import document_io
import main_csv_to_pickle
import text_processing


save_name = "save_04"
path_name = "text_processed"
if __name__ == "__main__":
    csv_pickle_name = main_csv_to_pickle.csv_pickle_name
    if not os.path.exists("obj/{}.pkl".format(csv_pickle_name)):
        raise FileNotFoundError("The file obj/{} doesn't exist, please run main_csv_to_pickle.py".format(csv_pickle_name))
    csv_file_under_dict_form = document_io.load(csv_pickle_name, '')
    number_of_lines = 1000000
    file_with_text_treated = text_processing.treat_text(csv_file_under_dict_form, number_of_lines)

    # Create the text corpus

    document_io.save(save_name, file_with_text_treated, path_name)
