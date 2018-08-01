def text_distance(vector_1, vector_2):
    """Compute the text similarity of vector_1 and vector_2, that are normalized vectors"""
    dot_product = 0
    for i in range(len(vector_1)):
        a_i_b_i = vector_1[i] * vector_2[i]
        dot_product += a_i_b_i
    return dot_product


def find_closest(target_key, dictionary):
    """Find the ticket that has the highest similarity to the ticket in input"""
    target_ticket = dictionary[target_key]
    target_vector = target_ticket['vector']
    max_similarity = -1
    number_of_tickets_explored = 0
    key_of_closest_ticket = target_key
    for ticket_number in dictionary.keys():
        vector_to_compare = dictionary[ticket_number]['vector']
        similarity = text_distance(target_vector, vector_to_compare)
        if similarity >= max_similarity and ticket_number != target_key:
            max_similarity = similarity
            key_of_closest_ticket = ticket_number
        number_of_tickets_explored += 1
    return max_similarity, target_key, key_of_closest_ticket
