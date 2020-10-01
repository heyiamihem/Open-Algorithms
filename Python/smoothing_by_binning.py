import numpy as np 
import math 

def equifreq(arr1, m): 
      
    a = len(arr1) 
    n = int(a / m) 
    for i in range(0, m): 
        arr = [] 
        for j in range(i * n, (i + 1) * n): 
            if j >= a: 
                break
            arr = arr + [arr1[j]] 
        print(arr) 


N=int(input("Enter the size of array:")) #take the size

data = list(map(int, input("Enter the array:").split(' ')[:N]))
data1 = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215] 

 
m = int(input("Enter the number of bin:")) 
  
n = int(N/m)
equifreq(data, m) 

b1 = np.zeros((n,m))
# Bin Mean 
for i in range (0,N,m): 
  k=int(i/m) 
  mean=(data[i] + data[i+1] + data[i+2] )/m
  for j in range(m): 
    b1[k,j]=mean 
print("Mean Bin:\n",b1)

b2 = np.zeros((n,m))
# Bin Median 
for i in range (0,N,m): 
  k=int(i/m) 
  for j in range (m): 
    b2[k,j]=data[i+1] 
print("Median Bin:\n",b2)


b3 = np.zeros((n,m))
#Bin Boundary
for i in range (0,N,m): 
  k=int(i/m) 
  for j in range (m): 
    if (data[i+j]-data[i]) < (data[i+2]-data[i+j]): 
      b3[k,j]=data[i] 
    else: 
      b3[k,j]=data[i+2]   
print("Boundary Bin:\n",b3)