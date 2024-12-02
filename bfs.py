graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

def bfs():
    visited=['A']
    queue=['A']
    seq=[]
    while queue:
        node=queue.pop(0)
        seq.append(node)
        for adjecent in graph[node]:
            if adjecent not in visited:
                queue.append(adjecent)
                visited.append(adjecent)
    
    for ele in seq:
        print(ele , end=' ')

bfs()
