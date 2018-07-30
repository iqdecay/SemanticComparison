import main_vectorization as vectorization
import document_similarity
import document_reading

file_name = vectorization.vector_file_name
dictionary = document_reading.load(file_name, 'vectorized_text')
tickets_to_treat = 10
if __name__ == "__main__":
    a = 0
    results = []
    keys = document_reading.load("samples", "others")
    print("Beginning testing of {} tickets".format(tickets_to_treat))
    for key in keys:
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
    document_reading.save("experience", results, 'results')
