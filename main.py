import csv_to_pickle as csv
import numpy as np
import text_processing
import document_io
import os
import gensim

# TODO : have the program ask for input
#  The csv file contains texts separated by commas
csv_filename = "enter filename with .csv"
base_name = "enter pickle name without extension"

# From the base name, initialize all of the filenames
pickle_name = base_name + ".pkl"

# If the pickle file exists, then go directly to treatment
cwd = os.getcwd()
complete_path = "{}/{}".format(cwd, pickle_name)
if not os.path.exists(complete_path):
    print("Pickle not found under {}, treating the csv".format(complete_path))
    csv_path = "{}/{}".format(cwd, csv_filename)
    file_dictionary = csv.open_csv(csv_path)
    csv.save_csv_as_pickle(file_dictionary, pickle_name)
else:
    print("Pickle found, not treating the CSV")
    file_dictionary = document_io.load(pickle_name)

""" Process text : 
 - tokenization
 - remove long and short words
 - remove punctuation and numbers
"""

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
    vector_length = 300  #  The Google W2V model has 300 dimensions
    sentence_vector = np.array([0 for _ in range(vector_length)])
    for word in sentence:
        try:
            sentence_vector = np.add(sentence_vector, np.array(w2v_model[word]))
        except KeyError:
            pass  # It just means the word isn't in the model
    return sentence_vector