def convert(adj_list, weighted=False):
    fill = float('inf') if weighted else 0
    n = len(adj_list)
    result = [[fill for i in range(n)] for i in range(n)]

    for i in range(n):
        result[i][i] = 0
        for j in adj_list[i]:
            if weighted:
                result[i][j] = adj_list[i][j]
            else:
                result[i][j] = 1

    return result


adj_list = {0: {1: 2, 2: 5}, 1: {2: 3}, 2: {0: 2, 3: 1}, 3: {2: 1}}
print(convert(adj_list, True))
