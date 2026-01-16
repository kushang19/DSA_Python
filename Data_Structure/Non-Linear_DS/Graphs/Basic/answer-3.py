# Number of Provinces

graph = {
    1: [3,7],
    2: [],
    3: [1,7],
    4: [9],
    5: [8,10],
    6: [8,10],
    7: [1,3],
    8: [5,6],
    9: [4],
    10: [5,6],
}

visited = set()
count = 0

def dfs(node):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

for node in graph:
    if node not in visited:
        count += 1
        dfs(node)

print(count)
