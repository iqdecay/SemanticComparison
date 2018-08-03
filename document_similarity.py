# Contains various fonctions to compute the semantical distance between two texts


def text_distance(vector_1, vector_2):
    """Compute the text similarity of vector_1 and vector_2, that are normalized vectors"""
    dot_product = 0
    for i in range(len(vector_1)):
        a_i_b_i = vector_1[i] * vector_2[i]
        dot_product += a_i_b_i
    return dot_product


def find_closest(target_key, dictionary):
    """
    Find the most similar ticket using dot product of two sentence vectors
    :param target_key: key of the ticket we want to find the "most similar" ticket
    :param dictionary: contains all the tickets, including their vector representation
    :return:
    max_similarity : biggest similarity found
    target_ticket : cf above
    key_of_closest_ticket : the closest ticket from target_ticket
    error : True if a KeyError occured, to avoid interrupting long computation
    """
    try:
        target_ticket = dictionary[target_key]
    except KeyError:
        print(target_key)
        return None, None, None, True
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
    return max_similarity, target_key, key_of_closest_ticket, False


def find_closest_wmd(target_key, dictionary, model):
    """
    Find the least dissimilar ticket using Word Mover's Distance (cf Research Paper)
    :param target_key: key of the ticket we want to find the "most similar" ticket
    :param dictionary: contains all the tickets, including their vector representation
    :param model: word2vec model
    :return:
    min_difference : least difference found
    target_ticket : cf above
    key_of_closest_ticket : the closest ticket from target_ticket
    error : True if a KeyError occured, to avoid interrupting long computation
    """
    try:
        target_ticket = dictionary[target_key]['body']
    except KeyError:
        print(target_key)
        return None, None, None, True
    min_difference = 1000
    number_of_tickets_explored = 0
    key_of_closest_ticket = target_key
    print("Testing")
    for ticket_number in dictionary.keys():
        current_ticket = dictionary[ticket_number]['body']
        difference = model.wmdistance(target_ticket, current_ticket)
        if difference <= min_difference and ticket_number != target_key:
            min_difference = difference
            key_of_closest_ticket = ticket_number
        number_of_tickets_explored += 1
        if number_of_tickets_explored % 1000 == 0:
            print("{} tickets explored so far".format(number_of_tickets_explored))
    print("WMD explored {} tickets".format(number_of_tickets_explored))
    return min_difference, target_key, key_of_closest_ticket, False
