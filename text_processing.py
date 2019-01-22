# Regroups all the function used to process the text in order to make it more "computer-friendly"
import string  # To remove punctuation from texts
import nltk
import tqdm



def is_stopword(word):
    """Return True if word is a stopword"""
    return word in tweaking.stop_words


def clean_characters(text):
    """Remove punctuation, numbers, and put the characters in lowercase"""
    punctuation_extended = string.punctuation + "'"  # Otherwise the ' character isn't deleted
    numbers = [str(i) for i in range(10)]
    cleaned_text = ""
    for char in text:
        if (char not in numbers) and (char not in punctuation_extended):
            cleaned_text += char.lower()
    return cleaned_text


def tokenize_text(text):
    """tokenize the text into words and return a list of token."""
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(text)
    return tokenized_text


def text_processing(text, min_len, max_len):
    """
    Take the input text, in string form, clean its characters, then tokenize it, then remove useless words,
    and words that are too long or too short and return it
    :param text: in string format
    :param min_len: the minimum length of a token to be considered a word
    :param max_len: the maximum length of a token to be considered a word
    :return: final_text under tokenized form, so a list of strings
    """
    new_text = str(text)
    text_cleaned = clean_characters(new_text)
    text_tokenized = tokenize_text(text_cleaned)
    final_text = []
    for word in text_tokenized:
        candidate = word
        if len(word) < min_len or len(word) > max_len:
            candidate = ''
        if is_stopword(word):
            candidate = ''
        if candidate != '':
            final_text.append(candidate)
    return final_text


def treat_text(dictionary, number_of_texts, min_len=4, max_len=15)
    """
    Open the dictionary, return a corpus of treated text from it
    :param dictionary: the dictionary which contains the texts
    :param number_of_texts: the number of texts that will be processed, can be limited for testing purposes
    :param min_len: the minimum length of a token to be considered a word
    :param max_len: the maximum length of a token to be considered a word
    :return: a corpus of text, under dictionary form
    """
    print("Beginning the text treatment of the file \n")
    text_treated = 0
    dict_with_treated_text = dict()
    for unique_id, text in tqdm.tqdm(dictionary.items()):
        new_text = text_processing(text, min_len, max_len)
        dict_with_treated_text[unique_id] = new_text
        text_treated += 1
        if text_treated > number_of_texts:
            break
    print("\n Text treatment finished")
    return dict_with_treated_text
