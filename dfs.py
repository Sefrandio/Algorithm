def dfs(matrix, start):
    stack = [start]
    visited = []

    while stack:
        current = stack.pop()
        visited.append(current)
        for node in range(len(matrix)):
            if matrix[current][node] != 0 and node not in visited:
                stack.append(node)
    return visited


print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
