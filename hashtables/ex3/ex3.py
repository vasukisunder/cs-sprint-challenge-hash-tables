def intersection(arrays):
    cache = {}
    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1
    
    result = []

    for i in cache:
        if cache[i] == len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
