from nltk import RegexpTokenizer
from string import punctuation  # To remove punctuation from texts
from tweaking import stop_words, replacement
from lemmatize import lemmatize_text


def is_stopword(word):
    """Return True if word is a stopword"""
    return word in stop_words


def clean_characters(text):
    """Remove punctuation, numbers, and put the characters in lowercase"""
    punctuation_extended = punctuation + "'"  # Otherwise the ' character isn't deleted
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
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(text)
    return tokenized_text


def is_short(word):
    return len(word) < 4


def is_long(word):
    return len(word) > 15


def text_processing(text, tree_tagger, clean=True, lemmatize=False, tokenize=True, remove_length=True,
                    remove_stopwords=True):
    new_text = str(text)
    if clean:
        new_text = clean_characters(new_text)
    if tokenize:
        new_text = tokenize_text(new_text)
    elif lemmatize:
        new_text = lemmatize_text(new_text, tagger=tree_tagger)
    else:
        raise TypeError('Either Lemmatize or Tokenize has to be True')
    final_text = []
    for word in new_text:
        candidate = word
        if candidate in replacement:
            candidate = replacement[candidate]
        if remove_length:
            if is_long(word) or is_short(word):
                candidate = ''
        if remove_stopwords:
            if is_stopword(word):
                candidate = ''
        if candidate != '':
            final_text.append(candidate)
    return final_text
