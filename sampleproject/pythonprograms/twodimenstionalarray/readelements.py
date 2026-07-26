import numpy as np

a = np.array([
    [2,4,6],
    [10,20,30]
])

print(a)
print("----------------------")
print("rows :", a.size, " Columns :",a[0].size)

for i in range(0, 2):
    for j in range(0, a[0].size):
        print(a[i,j], end=" ")
    print()

print("------------------")

for i in a:
    for j in i:
        print(j, end = " ")
    print()