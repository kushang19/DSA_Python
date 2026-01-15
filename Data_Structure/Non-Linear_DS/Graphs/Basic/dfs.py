# graph below is dictionary ds
graph = {
    "a" : ["b",'d'],
    "b" : [],
    "c" : [],
    "d" : ["e","g"],
    "e" : ['c'],
    "f" : [],
    "g" : ["f"],
}

def dfs(graph,source):
    stack = []
    stack.append(source)
    while stack:
        node  = stack.pop(-1)
        print(node,end=" ")
        for neighbour in graph[node]:
            stack.append(neighbour)

dfs(graph,'a')