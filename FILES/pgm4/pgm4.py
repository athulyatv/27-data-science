#4.	Write a program to compare two files

f = open('f1.txt', 'r')
data1=f.read()
file1 = open('f2.txt', 'r')
data2 = file1.read()
if data1 == data2:
    print("equal")
else:
    print("not equal")