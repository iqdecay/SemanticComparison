# Open the CSV file containing the data
import pickle
import tqdm
import os
from text_processing import text_processing
from tweaking import banned_ids
from lemmatize import define_tagger


def load(name, path):
    """Load an object stored in name.pkl pickle file in the obj folder"""
    print("Loading the object contained in obj/{}/{}.pkl \n".format(path, name))
    try:
        with open("obj/{}/{}.pkl".format(path, name), 'rb') as f:
            print("Loaded the object contained in obj/{}/{}.pkl \n".format(path, name))
            return pickle.load(f)
    except FileNotFoundError:
        print("The file was not found, are you sure about the file name ?")


def save(name, content, path):
    """Save object content in name.pkl file in the obj/path folder"""
    # If the file exists, we can save the new version under a new name, or not save at all
    if os.path.exists("obj/{}/{}.pkl".format(path, name)):
        choice = str(input("Do you want to overwrite the following file: obj/{}/{}.pkl (Y/N) ? ".format(path, name)))
        if choice.lower() == "y":
            print("Saving the object under obj/{}/{}.pkl".format(path, name))
            with open("obj/{}/{}.pkl".format(path, name), 'wb') as f:
                pickle.dump(content, f, -1)
            print("Object saved successfully under obj/{}/{}.pkl".format(path, name))
        else:
            new_name = input("Enter a new filename if you want to save, or 'N' to skip saving : ")
            if new_name.lower() != 'n':
                save(new_name, content, path)
            else:
                print("No file saved !")
                return None
    else:
        print("Saving the object under obj/{}/{}.pkl".format(path, name))
        with open("obj/{}/{}.pkl".format(path, name), 'wb') as f:
            pickle.dump(content, f, -1)
        print("Object saved successfully under obj/{}/{}.pkl".format(path, name))


def treat_text(file, number_of_texts):
    """
    Open the object "csv_file_as_pickle" and extract a text corpus from it
    :param file: the dictionary which content is modified
    :param number_of_texts: the number of texts that will be processed, can be limited for testing purposes
    :return: a corpus of text, that is the dictionary "csv_file_as_pickle" with the fields "subject" and
    "body" now containing the tokenized and treated version of their former content
    """
    print("Beginning the text treatment of the file \n")
    text_treated = 0
    dict_with_treated_text = dict()
    tree_tagger = define_tagger()
    for unique_id, ticket in tqdm.tqdm(file.items()):
        if unique_id not in banned_ids:
            dict_with_treated_text[unique_id] = dict(ticket)
            body = ticket['body']
            subject = ticket['subject']
            new_body = text_processing(body, tree_tagger)
            new_subject = text_processing(subject, tree_tagger)
            dict_with_treated_text[unique_id]['body'] = new_body
            dict_with_treated_text[unique_id]['subject'] = new_subject
            text_treated += 1
        if text_treated > number_of_texts:
            break
    print("\n Text treatment finished")
    return dict_with_treated_text
