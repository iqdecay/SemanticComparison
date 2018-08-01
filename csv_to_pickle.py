from document_io import save, load
import tqdm
import re

csv_pickle_name = 'csv_file_as_pickle'


def contains(string, sub_string):
    """Return True if sub_string is found in string"""
    return string.lower().find(sub_string) != -1


def cut_line(line):
    """Take a csv line and separate it into unique_id, subject and body, that are strings"""
    separator_index = line.find(";")  # The file is under the form: unique_id; subject; body;;;;;
    unique_id = line[:separator_index]  # The many ; at the end make it impractical to use the .split function
    line = line[separator_index + 1:]
    separator_index = line.find(";")
    subject = line[:separator_index]
    body = line[separator_index + 1:]
    clean_body = body.replace(';', '')  # Remove the useless ; signs
    return unique_id, subject, clean_body


def remove_tail(text):
    """Remove the tail of the text containing useless information and return it"""
    no_referrer = text.split('***')[0]
    no_cordialement = no_referrer.split('cordialement')[0]
    no_spam = no_cordialement.split('-- This message has been checked')[0]
    no_device = no_spam.split('Device')[0]
    no_info = no_device.split('**')[0]
    no_confidential = no_info.split("CONFIDENTIEL")[0]
    return no_confidential


def open_csv(filepath):
    """
    Open a csv file that uses ; as separators, and return a dictionary of dictionaries
    The text does not undergo cleaning, the "tail" of the body is simply removed.
    As the CSV file is supposed to be processed only once, all the lines are treated.
    The text is stored under string form.
    """
    nb = 0
    file_dictionary = dict()
    csv_file = open(filepath, encoding="ISO-8859-1")
    number_of_empty_body = 0
    pattern = re.compile(r'\s\s+')
    for line_ in tqdm.tqdm(csv_file):
        nb += 1
        line = str(line_)
        line = re.sub(pattern, ' ', line)  # Use regex to remove multiple space
        line = remove_tail(line)  # The tail contains irrelevant information
        unique_id, subject, body = cut_line(line)
        as_text = subject + "\n\n " + body
        as_text.replace("-", "\-")  # We add newline to make reading easier for "lists"
        if contains(subject, "re:") or contains(subject, "device") or contains(subject, "down"):
            body = ''
        body = re.sub('\\n', '', body)  # Use regex to remove newline characters
        if body != '':
            file_dictionary[unique_id] = {
                "text": str(as_text),
                "body": body,
                "subject": subject,
            }
        else:
            number_of_empty_body += 1
    print("The CSV {} was processed, there was {} lines with an empty body".format(filepath, number_of_empty_body))
    return file_dictionary


def save_csv_as_pickle(file_dict, filename):
    """Save the dictionary under pickle form"""
    save(filename, file_dict, '', overwrite=True)


if __name__ == '__main__':
    csv_name = 'tickets_with_unique_id_without_date.csv'
    dictionary_file = open_csv(csv_name)
    save_csv_as_pickle(dictionary_file, csv_pickle_name)
