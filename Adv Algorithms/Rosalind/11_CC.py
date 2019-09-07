import os
os.chdir("D:\\Downloads")
         

lines = map(lambda x: x.rstrip(), list(open("rosalind_cc.txt")))

V, E = map(int, lines[0].split())

if V == 1:
    print "1"
    exit()

adj = {}
for i in range(1, V+1):
    adj[i] = []
for edge in lines[1:]:
    src, dest = map(int, edge.split())
    adj[src].append(dest)
    adj[dest].append(src)

def explore(v):
    stack = adj[v]
    while len(stack) > 0:
        top = stack.pop()
        if not visited[top]:
            visited[top] = True
            stack += adj[top]

visited = [False] * (2+V)
connected_components = 0
for j in range(1, V+1):
    if not visited[j]:
        connected_components += 1
        explore(j)
print connected_components
