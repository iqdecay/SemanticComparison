import string  # To remove punctuation from texts

import nltk
import tqdm

import tweaking


def is_stopword(word):
    """Return True if word is a stopword"""
    return word in tweaking.stop_words


def clean_characters(text):
    """Remove punctuation, numbers, and put the characters in lowercase"""
    punctuation_extended = string.punctuation + "'"  # Otherwise the ' character isn't deleted
    numbers = [str(i) for i in range(10)]
    cleaned_text = ""
    for char in text:
        if char in ("'", "-"):
            char = ' '
        if (char not in numbers) and (char not in punctuation_extended):
            cleaned_text += char.lower()
    return cleaned_text


def tokenize_text(text):
    """tokenize the text into words and return a list of token."""
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(text)
    return tokenized_text


def is_short(word):
    return len(word) < 4


def is_long(word):
    return len(word) > 15


def text_processing(text):
    """
    Take the input text, in string form, clean its characters, then tokenize it, then remove useless words,
    and words that are too long or too short and return it
    :param text: in string format
    :return: final_text under tokenized form, so a list of strings
    """
    replacement = tweaking.replacement
    new_text = str(text)
    text_cleaned = clean_characters(new_text)
    text_tokenized = tokenize_text(text_cleaned)
    final_text = []
    for word in text_tokenized:
        candidate = word
        if candidate in replacement:
            candidate = replacement[candidate]
        if is_long(word) or is_short(word):
            candidate = ''
        if is_stopword(word):
            candidate = ''
        if candidate != '':
            final_text.append(candidate)
    return final_text


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
    for unique_id, ticket in tqdm.tqdm(file.items()):
        dict_with_treated_text[unique_id] = dict(ticket)
        body = ticket['body']
        subject = ticket['subject']
        new_body = text_processing(body)
        new_subject = text_processing(subject)
        dict_with_treated_text[unique_id]['body'] = new_body
        dict_with_treated_text[unique_id]['subject'] = new_subject
        text_treated += 1
        if text_treated > number_of_texts:
            break
    print("\n Text treatment finished")
    return dict_with_treated_text
