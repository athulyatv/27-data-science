#1.	Write a program to copy a text file to another file

with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)