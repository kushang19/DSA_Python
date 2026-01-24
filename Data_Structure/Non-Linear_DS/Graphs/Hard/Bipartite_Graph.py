graph = {
    1: [2],
    2: [1,3,6],
    3: [2,4],
    4: [3,5,7],
    5: [4,6],
    6: [2,5],
    7: [4,8],
    8: [7]
}

color = [-1] * (len(graph) + 1)   # color[i] = -1 means unvisited

# def is_bipartite(graph, color):

#     for start in graph:   # to handle disconnected graphs
#         if color[start] != -1:
#             continue

#         stack = [start]
#         color[start] = "G"   # start coloring with G

#         while stack:
#             node = stack.pop()

#             # Decide opposite color for neighbors
#             next_color = "Y" if color[node] == "G" else "G"

#             for neighbour in graph[node]:
#                 # if neighbour is not colored, color it and push
#                 if color[neighbour] == -1:
#                     color[neighbour] = next_color
#                     stack.append(neighbour)

#                 # if already colored, it must be opposite
#                 elif color[neighbour] != next_color:
#                     return False

#     return True


# print(is_bipartite(graph, color))
# print(color)



# If you want recursive DFS version (also correct)

def dfs(node, c):
    color[node] = c
    next_color = "Y" if c == "G" else "G"

    for neighbour in graph[node]:
        if color[neighbour] == -1:
            if not dfs(neighbour, next_color):
                return False
        elif color[neighbour] != next_color:
            return False

    return True

def is_bipartite_recursive(graph):
    for node in graph:
        if color[node] == -1:
            if not dfs(node, "G"):
                return False
    return True

print(is_bipartite_recursive(graph))
print(color)
