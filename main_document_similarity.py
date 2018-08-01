import shutil
import tqdm

import main_vectorization as vectorization
import document_similarity
import document_io

file_name = vectorization.vector_file_name
number_of_features = 250
dictionary = document_io.load("save_04_vectorized_{}".format(number_of_features), 'vectorized_text')
experience_name = "big_results"
if __name__ == "__main__":
    print(experience_name)
    results = []
    keys = document_io.load("3000_tickets", "others")
    tickets_to_treat = len(keys)
    print("Beginning testing of {} tickets".format(tickets_to_treat))
    for key in tqdm.tqdm(keys):
        max_similarity, target_key, closest_key, error = document_similarity.find_closest(key, dictionary)
        if not error:
            result = {"ticket_a": target_key,
                      "ticket_b": closest_key,
                      "similarity": max_similarity,
                      }
            results.append(result)
    print("Finished testing of {} tickets".format(a))
    document_io.save(experience_name, results, 'results')
    relative_path = "C:/Users/clbr-vnepveu/Desktop/Victor/code/code_victor/"
    shutil.copyfile("{}obj/results/{}.pkl".format(relative_path, experience_name),
                    "{}/obj/experience/{}.pkl".format(relative_path, experience_name))
