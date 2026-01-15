# graph below is dictionary ds
graph = {
    "a" : ["b",'c'],
    "b" : ["f","d"],
    "c" : [],
    "d" : ["g","i"],
    "e" : ['h'],
    "f" : ["e"],
    "g" : [],
    "h" : ["g"],
    "i" : [],
}


def hasPath(src,dist,graph):
    if src == dist:
        return True

    ans = False
    for neighbour in graph[src]:
        ans = ans or hasPath(neighbour, dist, graph) 
    
    return ans


src = "a"
dist = "d"

print(hasPath(src,dist,graph))