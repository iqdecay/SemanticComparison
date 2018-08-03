import gensim.models
import numpy as np
from document_io import save
import tqdm


def load_model(model_name):
    """Load the Word2Vec model saved under model_name and return it"""
    return gensim.models.Word2Vec.load(model_name)


def sentence_to_vect(sentence, w2v_model):
    """
    Transform the sentence into a normalized vector by linear addition of its composing word vectors
    :param sentence: tokenized sentence, as word list
    :param w2v_model: word2vec model, already trained
    :return: the corresponding vector, and wether or not it is null
    """
    vector_length = len(w2v_model['ximi'])  # We use ximi because we know it's in the model's vocabulary
    sentence_vector = np.array([0 for _ in range(vector_length)])
    for word in sentence:
        try:
            sentence_vector = np.add(sentence_vector, np.array(w2v_model[word]))
        except KeyError:
            pass  # It just means the word isn't in the model
    norm_vector = np.linalg.norm(sentence_vector)
    if norm_vector != 0:
        sentence_vector = sentence_vector / norm_vector
        has_null_vector = False
    else:
        has_null_vector = True
    return sentence_vector, has_null_vector


def transform_ticket(ticket, model):
    """"Transform the ticket into a vector, add the vector to the ticket and return the ticket"""
    body = ticket['body']
    sentence = list(body)  # One will notice that at no point is the subject taken into account
    vectorized, has_null_vector = sentence_to_vect(sentence, model)
    ticket['vector'] = vectorized
    return ticket, has_null_vector


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
