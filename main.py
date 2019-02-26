import csv_to_pickle as csv
import numpy as np
import text_processing
import document_io
import os
import gensim
import text_similarity

# TODO : have the program ask for input
cwd = os.getcwd()
#  The csv file contains texts separated by commas
csv_filename = "enter filename with .csv"
base_name = "enter pickle name without extension"

if not os.path.exists("{}/{}".format(cwd, csv_filename)):
    raise FileNotFoundError("The csv file isn't in the current working directory")

# From the base name, initialize all of the filenames
pickle_name = base_name + ".pkl"

# If the pickle file exists, then go directly to treatment
complete_path = "{}/{}".format(cwd, pickle_name)
if not os.path.exists(complete_path):
    print("Pickle not found under {}, treating the csv".format(complete_path))
    csv_path = "{}/{}".format(cwd, csv_filename)
    file_dictionary = csv.open_csv(csv_path)
    csv.save_csv_as_pickle(file_dictionary, pickle_name)
else:
    print("Pickle found, not treating the CSV")
    file_dictionary = document_io.load(pickle_name)

number_of_texts = len(file_dictionary)

# TODO : handle the choice of language, defaulting to english for now

treated_dictionary_pickle_name = base_name + "_treated_dict" + ".pkl"

# If the treated text exists, do not run the treatment again
if not os.path.exists("{}/{}".format(cwd, treated_dictionary_pickle_name)):
    #  Specify the parameters, cf text_processing.py for explanation
    treated_dictionary = text_processing.treat_dictionary(file_dictionary, min_len=1, max_len=15)
    document_io.save(treated_dictionary_pickle_name, treated_dictionary, cwd)
    print("The text was treated and saved under {}{}".format(cwd, treated_dictionary_pickle_name))
else:
    print("Treated text was found, not processing it")
    treated_dictionary = document_io.load(treated_dictionary_pickle_name)

# Use the pre-trained Google News model

model = gensim.models.Word2Vec.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)


# TODO : add possibility to train your own model on a corpus, but specify the type of the corpus


def sentence_to_vector(sentence):
    """
    Transform the sentence into a normalized vector by linear addition of its composing word vectors
    :param sentence: tokenized sentence, as word list
    :return: the corresponding vector
    """
    global model
    vector_length = 300  #  The Google W2V model has 300 dimensions
    sentence_vector = np.array([0 for _ in range(vector_length)])
    for word in sentence:
        try:
            sentence_vector = np.add(sentence_vector, np.array(model[word]))
        except KeyError:
            pass  # It just means the word isn't in the model
    return sentence_vector


vectorized_text_pickle_name = base_name + "vectorized_text" + ".pkl"

vectorized_texts = dict()

# Vectorize every sentence
for key, tokenized_sentence in treated_dictionary.items():
    vectorized_sentence = sentence_to_vector(tokenized_sentence)
    vectorized_texts[key] = vectorized_sentence

# Save the result
document_io.save(vectorized_text_pickle_name, vectorized_texts, cwd)


def find_closest(target_key):
    """
    Find the most similar ticket using dot product of two sentence vectors
    :param target_key: key of the sentence we want to find the "most similar" sentence for
    :return:
    max_similarity : biggest similarity found
    closest_key : the key of closest sentence
    """
    global vectorized_texts
    target_vector = vectorized_texts[target_key]
    max_similarity = -1
    closest_key = target_key
    for key, sentence_vector in vectorized_texts.items():
        similarity = text_similarity.text_distance(target_vector, sentence_vector)
        if similarity >= max_similarity and key != target_key:
            max_similarity = similarity
            closest_key = key
    return max_similarity, closest_key
