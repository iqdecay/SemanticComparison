# Allows creating and saving of a Word2Vec model with tunable parameters
import gensim.models
import logging


def create_model(text_corpus, n_features=100, window_size=100, min_word_count=100, downsample=0.001):
    """
    Return the trained Word2Vec model and provide information about the training.
    :param text_corpus: the corpus of text, a list of tokenized sentences
    :param n_features: the number of features used for the model, too much mean higher probability of overfitting
    :param window_size: number of words taken before and after the target word, for context during training
    :param min_word_count: minimum number of times the word has to appear in the corpus
    :param downsample: rate of downsampling, inversely proportional to the number of most-common words removed
    :return: the trained Word2Vec model
    """
    logging_format = "%(asctime)s : %(levelname)s : %(message)s"
    logging.basicConfig(format=logging_format, level=logging.INFO)  # Logging for model training
    # Creating and training the model
    model = gensim.models.Word2Vec(text_corpus, size=n_features, window=window_size, min_count=min_word_count,
                                   workers=8, sample=downsample)
    return model


def save_model(model, model_save_name):
    """Save the provided model under the provided name"""
    model.save(model_save_name)
    print('Model saved under name : {}'.format(model_save_name))
