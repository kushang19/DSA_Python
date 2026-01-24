# ================= number of provinces ========================


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
    10: [5,6]
}

vis = set()

def dfs(graph, src, vis):
    vis.add(src)
    for neighbour in graph[src]:
        if neighbour not in vis:
            dfs(graph, neighbour, vis)
   
def no_of_provinces(graph, vis):
    count = 0
    for i in graph:
        if i not in vis:
            count += 1
            dfs(graph, i, vis)
           
   
    return count
       
   
print(no_of_provinces(graph, vis))