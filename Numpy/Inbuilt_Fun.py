import numpy as np
Zeros=np.zeros((3,3))
print(Zeros)
Ones=np.ones((2,4))
print(Ones)
Identity=np.eye(3,3)
print(Identity)
random_arr=np.random.randint(low=3,high=20,size=10)# For integer in a given range
random_arr_float=np.random.rand(10) #For Float values
print(random_arr_float)
print(random_arr)