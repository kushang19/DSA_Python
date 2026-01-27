class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node):
    if not node:
        return None

    visited = {}

    def dfs(curr):
        if curr in visited:
            return visited[curr]

        clone = Node(curr.val)
        visited[curr] = clone

        for nei in curr.neighbors:
            clone.neighbors.append(dfs(nei))

        return clone

    return dfs(node)

# pending 
# 1: [2,4]
# 2: [1,3]
# 3: [2,4]
# 4: [1,3]
