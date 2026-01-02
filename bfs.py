from collections import deque


def bfs(pairs):
    queue = deque([['', 0, 0]])
    result = []

    while queue:
        current, open, close = queue.popleft()
        if len(current) == pairs * 2:
            result.append(current)
        if open < pairs:
            queue.append([current + '(', open + 1, close])
        if close < open:
            queue.append([current + ')', open, close+1])
    return result


print(bfs(2))
