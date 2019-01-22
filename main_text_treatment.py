import os
import document_io
import text_processing

if __name__ == "__main__":
    pickle_path = input("Enter the name path to the pickle file you want to treat, relative to the cwd : \n")
    if not os.path.exists(pickle_path):
        raise FileNotFoundError(
            "The file {} doesn't exist, please run main_csv_to_pickle.py".format(pickle_path))

    csv_file_under_dict_form = document_io.load(pickle_path)
    file_with_text_treated = text_processing.treat_text(csv_file_under_dict_form, number_of_lines)

    # Create the text corpus

    treated_text_path = input("Enter the name path you want to save the treated text to : \n")
    document_io.save(save_name, file_with_text_treated, path_name)
