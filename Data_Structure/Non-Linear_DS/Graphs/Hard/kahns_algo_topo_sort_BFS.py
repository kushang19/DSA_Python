from collections import deque

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2],
}

n = len(graph)

# ✅ indegree array
in_degree = [0] * n

# ✅ Calculate indegree of each node
for node in graph:
    for neighbour in graph[node]:
        in_degree[neighbour] += 1

print("in_degree:", in_degree)

# ✅ Push all nodes with indegree 0 into queue
queue = deque()
for node in range(n):
    if in_degree[node] == 0:
        queue.append(node)

print("initial queue:", queue)

# ✅ Kahn's BFS
topo = []

while queue:
    node = queue.popleft()
    topo.append(node)

    for neighbour in graph[node]:
        in_degree[neighbour] -= 1

        if in_degree[neighbour] == 0:
            queue.append(neighbour)

print("Topological Order:", topo)



# ✅ Topological Sort (BFS / Kahn) for Alphabetic Nodes

# from collections import deque

# graph = {
#     "A": ["C"],
#     "B": ["C", "D"],
#     "C": ["E"],
#     "D": ["F"],
#     "E": [],
#     "F": []
# }

# def topo_sort_alpha(graph):
#     in_degree = {node: 0 for node in graph} #{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}


#     # count indegrees
#     for node in graph:
#         for neighbour in graph[node]:
#             in_degree[neighbour] += 1
    
#     print(in_degree,'oooo')

#     # queue all nodes with indegree 0
#     queue = deque([node for node in graph if in_degree[node] == 0])

#     topo = []

#     while queue:
#         node = queue.popleft()
#         topo.append(node)

#         for neighbour in graph[node]:
#             in_degree[neighbour] -= 1
#             if in_degree[neighbour] == 0:
#                 queue.append(neighbour)

#     # cycle check
#     if len(topo) != len(graph):
#         return "Cycle detected ❌ (Topological sort not possible)"

#     return topo


# print(topo_sort_alpha(graph))
