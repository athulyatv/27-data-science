import numpy as np
m=int(input("Enter no of rows : "))
n=int(input("Enter no of cols : "))
print("Enter ",m*n," elements : ")
arr=np.array([])
for i in range(m*n):
    e=int(input())
    arr=np.append(arr,e)
arry = arr.astype(int)

print("The Matrix is  : ")

mat=arry.reshape(m,n)
print(mat)

print("Number of rows from the matrix is : ")
print(mat.shape[0])

print("Number of columns from the matrix is : ")
print(mat.shape[1])