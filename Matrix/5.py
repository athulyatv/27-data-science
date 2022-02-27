import numpy as np
m=int(input("Enter no of rows : "))
n=int(input("Enter no of cols : "))
print("Enter ",m*n," elements for first matrix : ")
arr=np.array([])
for i in range(m*n):
    e=int(input())
    arr=np.append(arr,e)
arry = arr.astype(int)

print("Enter ",m*n," elements for second matrix : ")
arra=np.array([])
for j in range(m*n):
    v=int(input())
    arra=np.append(arra,v)
arri = arra.astype(int)

print("The first Matrix is  : ")

mat1=arry.reshape(m,n)
print(mat1)

print("The second Matrix is  : ")

mat2=arri.reshape(m,n)
print(mat2)

add=np.add(mat1,mat2)
print("Addition of two matrix is : ",add)


print("Substraction of two matrix is : ",np.subtract(mat1,mat2))

print("Division of two matrix is : ",np.divide(mat1,mat2))
