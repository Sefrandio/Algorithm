import heapq
from adj_matrix_to_adj_list import convert

INF = float('inf')
matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def djikstra(matrix, start, target=None):
    n = len(matrix)
    distances = [INF]*n
    distances[start] = 0
    visited = [False]*n
    paths = [[] for i in range(n)]
    paths[start] = [start]
    for node in range(n):
        current = -1
        min_distance = INF
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                current = i
                min_distance = distances[i]
        if current == -1:
            break

        visited[current] = True

        for i in range(n):
            distance = matrix[current][i]
            if not visited[i] and distance != INF:
                current_distance = distances[current] + distance
                if current_distance < distances[i]:
                    distances[i] = current_distance
                    paths[i] = paths[current] + [i]

    out = ''
    target = [target if target != None else i for i in range(n)]
    for i in target:
        route = ' -> '.join(map(str, paths[i]))
        out += f'the path from {start} to {i} is {route} and the distance is {distances[i]}\n'

    return out


print(djikstra(matrix, 3))
