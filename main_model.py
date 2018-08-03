# Create a Word2Vec model based off the treated tickets, assembled into a corpus
import document_io
import manage_model
from main_text_treatment import save_name

model_name = save_name + '_model_50_no_subject'
if __name__ == "__main__":
    file_with_text_treated = document_io.load(save_name, 'text_processed')
    text_corpus = []
    for unique_id, ticket in file_with_text_treated.items():
        treated_text = ticket['body']
        if treated_text != list():
            text_corpus.append(treated_text)
    number_of_features = 50
    window_size = 5
    sample = 0.001
    word_count_min = 2
    model = manage_model.create_model(text_corpus,
                                      n_features=number_of_features,
                                      window_size=window_size,
                                      min_word_count=word_count_min
                                      )
    manage_model.save_model(model, "obj/models/{}".format(model_name))
    words_with_their_count = list()
    for key, word_object in model.wv.vocab.items():
        words_with_their_count.append((word_object.count, key))
    words_with_their_count.sort(reverse=True)
    for i in range(20):
        print(words_with_their_count[i])
