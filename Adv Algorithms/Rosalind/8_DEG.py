import os
from collections import Counter
from itertools import chain
os.chdir('D:\\Desktop')

edges = []
with open('rosalind_deg.txt') as f:
    next(f)
    for line in f:
        edges.append(line.strip().split())
f.close()


my_list = []
for x in chain.from_iterable(edges):
    my_list.append(x)

d = Counter(my_list)
for key in sorted(d, key = int):
    print(d[key], end = " ")
