# Find Shortest part for an unweighted graph

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": [],
}

src = "A"
target = "D"

def shortest_path(graph,src,target):
    queue = [(src,0)]
    visit = {src}

    while queue != []:
        node, dist = queue.pop(0)

        if node == target:
            return dist
        
        # for neighbour in graph[node]:      
        # If graph[node] does not exist → KeyError below is the Safer method
        
        for neighbour in graph.get(node, []): 
            if neighbour not in visit:
                visit.add(neighbour)
                queue.append((neighbour, dist + 1))

    return -1


print(shortest_path(graph,src,target))