import os
import collections
os.chdir('D:\\Downloads')

f = open('rosalind.txt')
documentread = f.read()
def directed_graph( vertices, dedges ) :
    V = [ v for v in range(1,vertices+1) ]
    d_graph = collections.defaultdict(set)
    for edge in dedges :
        d_graph[edge[0]].add(edge[1])
    return [ V, d_graph ]

def topological_sort(from_lists, to_lists):
    visited = [False] * len(from_lists)
    sequence = []
    for i in range(len(visited)):
        if not visited[i] and len(from_lists[i]) == 0:
            dfs(from_lists, to_lists, visited, sequence, i)
    return sequence
    

def get_toposort(num_vertices, edges ):
    d_graph = directed_graph(num_vertices, edges )
    vertices = [ n for n in range(1,num_vertices+1)]
    postorder = toposorted(vertices, d_graph )
    return reversed(postorder)

filein = open("rosalind_ts.txt")
data = filein.read()
print(data)
linesin = [ sublist.strip().split() for sublist in data.splitlines() ]
edges = [ [ int(edge[0]), int(edge[1]) ] for edge in linesin ]


print ( linesin )

#outnums = get_topo_sort(edges[0][0], edges[1:])

filein.close()
