import os
os.chdir("D:\\Downloads")
f = open("rosalind_ini5.txt")
count = 1
for line in f.readlines():
   if count % 2 == 0:
        print (line)
   count +=1
