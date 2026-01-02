def convert(matrix, weighted=False):
    n = len(matrix)
    if weighted:
        result = {i: {} for i in range(n)}
    else:
        result = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and weighted:
                result[i][j] = matrix[i][j]
            elif matrix[i][j] != 0 and not weighted:
                result[i].append(j)

    return result


print(convert([[0, 1, 1, 0], [0, 0, 1, 0],
               [1, 0, 0, 1], [0, 0, 1, 0]], False))
