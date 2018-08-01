import shutil
import tqdm

import main_vectorization as vectorization
import document_similarity
import document_io

file_name = vectorization.vector_file_name
number_of_features = 1000
dictionary = document_io.load("save_04_vectorized_{}".format(number_of_features), 'vectorized_text')
tickets_to_treat = 3000
experience_name = "big_results"
if __name__ == "__main__":
    a = 0
    results = []
    keys = document_io.load("3000_tickets", "others")
    print("Beginning testing of {} tickets".format(tickets_to_treat))
    for key in tqdm.tqdm(keys):
        max_similarity, target_key, closest_key = document_similarity.find_closest(key, dictionary)
        result = {"ticket_a": target_key,
                  "ticket_b": closest_key,
                  "similarity": max_similarity,
                  }
        results.append(result)
        a += 1
        if a >= tickets_to_treat:
            break
    print("Finished testing of {} tickets".format(a))
    document_io.save(experience_name, results, 'results')
    relative_path = "C:/Users/clbr-vnepveu/Desktop/Victor/code/code_victor/"
    shutil.copyfile("{}obj/results/{}.pkl".format(relative_path, experience_name),
                    "{}/obj/experience/{}.pkl".format(relative_path, experience_name))
