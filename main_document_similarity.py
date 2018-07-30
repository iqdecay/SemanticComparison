import main_vectorization as vectorization
import document_similarity
import document_reading

file_name = vectorization.vector_file_name
dictionary = document_reading.load(file_name, 'vectorized_text')
if __name__ == "__main__":
    a = 0
    results = dict()
    keys = document_reading.load("samples", "others")
    similarity = list()
    text_target = list()
    text_closest = list()
    print("Beginning testing")
    for key in keys:
        max_similarity, target_key, closest_key = document_similarity.find_closest(key, dictionary)
        results[target_key] = {
                                "target_text": dictionary[target_key]['text'],
                                "closest_text": dictionary[closest_key]['text'],
                                "similarity": max_similarity,
        }
        a += 1
        text_target.append(results[target_key]["target_text"])
        text_closest.append(results[target_key]["closest_text"])
        similarity.append(similarity)
        if a > 200:
            break

    document_reading.save("results_"+file_name, results, 'results')
