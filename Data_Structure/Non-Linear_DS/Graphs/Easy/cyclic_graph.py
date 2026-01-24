# ========================= cyclic graph  ========================
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

visit = set()
src = "h"
dst = "c"
def hasDirectedPath(graph, src, dst, visit):
    if src == dst:
        return True
    visit.add(src)
    ans = False
    for neighbour in graph[src]:
        if neighbour not in visit:
            ans = ans or hasDirectedPath(graph, neighbour, dst, visit)
    return ans
   
print(hasDirectedPath(graph, src, dst, visit))