import re
import string
import os
from collections import defaultdict
os.chdir('/Users/ebenschumann/Downloads')
frequency = defaultdict(lambda:0)
#a = 'We tried list and we tried dicts also we tried Zen'
document_text = open('rosalind_ini6 (1).txt')
document = document_text.read()
#text_string = 
#match_pattern = re.findall(r'\b[a-z,A-Z]{2,15}\b', text_string)

match_pattern = [word for line in document.splitlines() for word in line.strip().split()] 
for word in match_pattern:
    #count = frequency.get(word,0)
    frequency[word.strip()] += 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])
