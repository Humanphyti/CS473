import os
from bisect import bisect_left
#os.chdir('D:\\Downloads')
os.chdir('/Users/ebenschumann/Downloads')

def binary_search(lst, target, high):
        i = bisect_left(lst, target)
        if i != high and lst[i] == item:
                return i + 1
        else:
                return -1

linesin = open('rosalind.txt')
data = linesin.strip().split() for line in linesin.splitlines()
n = int(data[0][0])
m = int(data[1][0])
sorted_array = list(map(int, data[2]))
list_int = list(map(int, data[2]))

result = []
for item in list_int:
        result.append(binary_search(sorted_array, item, n))

result = list(map(str, result))

linesin.close()
fileout = open('rosalind_mer.txt', 'w+')
fileout.write(' '.join(result))
fileout.close()
