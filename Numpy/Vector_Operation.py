import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])
#Elements wise operation
print("Addition:",arr1+arr2)
print("Substraction:",arr1-arr2)
print("Multiplication:",arr1*arr2)
print("Division:",arr1/arr2)

#Broadcasting
arr=np.array([1,2,3])
mat=np.array([[1,2,3],[4,5,6]])
print(mat+arr)