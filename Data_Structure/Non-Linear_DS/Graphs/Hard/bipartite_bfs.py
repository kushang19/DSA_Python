from collections import deque
graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3]
}

def is_bipartite_bfs(graph):
    color = {}  # node -> 0 or 1

    for start in graph:  # handles disconnected components
        # if start in color:
        #     continue

        print(start)

        queue = deque([start])
        color[start] = 0  # start coloring with 0

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                # If not colored, assign opposite color
                if neighbour not in color:
                    color[neighbour] = 1 - color[node]
                    queue.append(neighbour)

                # If already colored and same as current -> conflict
                elif color[neighbour] == color[node]:
                    return False

    return True


print(is_bipartite_bfs(graph))