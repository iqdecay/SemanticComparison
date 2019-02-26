import gensim.models
import numpy as np
from document_io import save
import tqdm


def load_model(model_name):
    """Load the Word2Vec model saved under model_name and return it"""
    return gensim.models.Word2Vec.load(model_name)


def sentence_to_vector(sentence, w2v_model):
    """
    Transform the sentence into a normalized vector by linear addition of its composing word vectors
    :param sentence: tokenized sentence, as word list
    :param w2v_model: word2vec model, already trained
    :return: the corresponding vector
    """
    vector_length = 300  #  The Google W2V model has 300 dimensions
    sentence_vector = np.array([0 for _ in range(vector_length)])
    for word in sentence:
        try:
            sentence_vector = np.add(sentence_vector, np.array(w2v_model[word]))
        except KeyError:
            pass  # It just means the word isn't in the model
    return sentence_vector


def save_to_memory(key_list, value_list, filename, w2v_model):
    """
    Compute tickets' sentence vectors and save it
    :param key_list: list of the keys of the dictionnary
    :param value_list: list of the values of the dictionnary
    :param filename: name of the pickle file it will be saved under (given without the .pkl extension)
    :param w2v_model: the w2v model that contains the word vectors, already trained
    :return: None
    """
    object_to_save = dict()
    object_length = len(key_list)
    number_of_null_vectors = 0
    if len(value_list) != object_length:
        raise IndexError("The two provided lists don't have the same length")
    for i in tqdm.tqdm(range(object_length)):
        value = value_list[i]
        new_ticket, has_null_vector = transform_ticket(value, w2v_model)
        if has_null_vector:
            number_of_null_vectors += 1
        object_to_save[key_list[i]] = new_ticket
    print("There was {} null vectors".format(number_of_null_vectors))
    save(filename, object_to_save, "vectorized_text")
    return None
