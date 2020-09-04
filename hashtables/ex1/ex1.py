def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for i in range(length):
        difference = limit - weights[i]
        if difference in cache:
            return [i, cache[difference]]
        else:
            cache[weights[i]] = i



    return None
