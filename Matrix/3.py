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

sumv=np.sum(mat)
print("Sum of values in the matrix is : ",sumv)