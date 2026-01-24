# ===========  Detect a Cycle in an Undirected Graph using BFS  ===============

from collections import deque

graph ={
    1: [2,3],
    2: [1,5],
    3: [1,4,6],
    4: [3],
    5: [2,7],
    6: [3,7],
    7: [5,6]
}

def cycle_checking(graph):
    visit = set()
   
    def bfs(start):
        queue = deque()
        queue.append((start, -1))
        visit.add(start)

        while queue:
            node, parent = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in visit:
                    queue.append((neighbour, node))
                    visit.add(neighbour)
                elif neighbour != parent:
                    return True

        return False
       
    for node in graph:
        if node not in visit:
            if bfs(node):
                return True
    return False
       
print(cycle_checking(graph))




# ===========  Detect a Cycle in an Undirected Graph using DFS  ===============

from collections import deque

graph ={
    1: [2,4],
    2: [1,5],
    3: [4,6],
    4: [1,3],
    5: [2,7],
    6: [3,7],
    7: [5,6]
}

def cycle_checking(graph):
    visit = set()
   
    def dfs(start):
        stack = []
        stack.append((start, -1))
        visit.add(start)

        while stack:
            node, parent = stack.pop()

            for neighbour in graph[node]:
                if neighbour not in visit:
                    stack.append((neighbour, node))
                    visit.add(neighbour)
                elif neighbour != parent:
                    return True

        return False
       
    for node in graph:
        if node not in visit:
            if dfs(node):
                return True
    return False
       
print(cycle_checking(graph))