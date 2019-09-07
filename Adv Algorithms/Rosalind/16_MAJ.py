from collections import Counter
import os
os.chdir('D:\\Downloads')


if __name__ == '__main__':
    # read data
    f =  open(os.path.join(os.path.split(os.getcwd())[0], "D:\\Downloads", "rosalind_maj.txt"), 'r')
    data = [map(int, line.rstrip().split()) for line in f.readlines()]
    firstline = data.pop(0)
    k, n = firstline[0], firstline[1]

    cutoff = n/2
    max_elem = []

    for line in data:
        freqs = Counter(line)
        if any(t > cutoff for t in freqs.values()):
            max_elem.append(max(freqs, key=freqs.get))
        else:
            max_elem.append(-1)

    # save output file
    outhandle = open(os.path.join(os.path.split(os.getcwd())[0], "D:\\Downloads", "rosalind_mer.txt"), 'w')
    print >> outhandle, " ".join(map(str, max_elem))
    outhandle.close()
