# Merge 2 Sorted Arrays
import os
os.chdir('D:\\Downloads')

f = open('rosalind_mer.txt')

sizeA = f.readline()

arrayA = f.readline().split()

sizeB = f.readline()

arrayB = f.readline().split()


def merge( arrayA, arrayB, results):
    if len(arrayA) > len (arrayB):
        maxlength = len(arrayA)
        minlength = len(arrayB)
    else:
        maxlength = len(arrayB)
        minlength = len(arrayA)
    while arrayA and arrayB:
        #print(arrayA[0])
        a = int(arrayA[0])
        b = int(arrayB[0])    
        if a <= b:
            results.append(a)
            arrayA.pop(0)
        else:
            results.append(b)
            arrayB.pop(0)
    while arrayA:
        a = int(arrayA[0])
        results.append(a)
        arrayA.pop(0)
    while arrayB:
        b = int(arrayB[0])
        results.append(b)
        arrayB.pop(0)

f.close()
results = []
mer = merge(arrayA, arrayB, results)
#fileout = open('rosalind_mer.txt', 'w+')
print (results)

