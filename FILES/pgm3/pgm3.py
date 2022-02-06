#3.	Write a program to count the frequencies of each word from a file
from collections import Counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print('Number of words in the file :',word_count('t.txt'))
