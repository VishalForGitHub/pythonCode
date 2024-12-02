graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

def dfs():
    visited=['A']
    dfs=[]
    stack=['A']
    while stack:
        val=stack.pop()
        dfs.append(val)
        for adjacent in graph[val]:
            if adjacent not in visited:
                stack.append(adjacent)
                visited.append(adjacent)
    
    for seq in dfs:
        print(seq, end=' ')


dfs()