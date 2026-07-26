import numpy as np

x=np.array([
    [10,20,30],
    [40,50,60]
])

y=np.array([
    [1,2,3],
    [4,5,6]
])

for i in range(0,2):
    for j in range(0,3):
        result=x[i,j] + y[i,j]
        print(result, end=" ")
    print()