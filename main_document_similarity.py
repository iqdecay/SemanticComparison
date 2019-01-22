# This file handles finding the most similar ticket to all the tickets given in input. It does this by using two
# different methods.  One is simply computing the dot product of the two sentence vectors.
# The other is using Word Mover's Distance, a novel and optimized, but performance-intensive, technique
# that makes the most of the word embedding allowed by Word2Vec
# More info : "From Word Embeddings To Document Distances", research paper by Kusner & al.
import tqdm
import main_vectorization as vectorization
import document_similarity
import document_io
import text_2_vec

file_name = vectorization.vector_file_name
number_of_features = 50
dictionary = document_io.load("save_04_vectorized_{}_no_subjects".format(number_of_features), 'vectorized_text')
experience_name = "handpicked_50"
if __name__ == "__main__":
    print(experience_name)
    results = []
    keys = document_io.load("aggregate", "others")
    tickets_to_treat = len(keys)
    print("Beginning testing of {} tickets".format(tickets_to_treat))
    model = text_2_vec.load_model("obj/models/save_04_model_50_no_subject")
    # For each ticket, we find the closest by using the two different algorithms
    # A major drawback is the computing time : about 15 min for Word Mover's Distance
    for key in tqdm.tqdm(keys):
        max_similarity, target_key, closest_key, error = document_similarity.find_closest(key, dictionary)
        min_difference, _, closest_key_wmd, error = document_similarity.find_closest_wmd(key, dictionary, model)
        if not error:
            text_target = dictionary[target_key]["text"]
            text_wmd = dictionary[closest_key_wmd]["text"]
            text_classic = dictionary[closest_key]["text"]
            print(text_target)
            print(text_classic)
            print(text_wmd)
            print("Similarity : {}, Difference : {}".format(max_similarity, min_difference))
        else:
            print("There was a KeyError with key {}".format(target_key))
    print("Finished testing of {} tickets".format(tickets_to_treat))
    document_io.save(experience_name, results, 'results')
