import numpy as np
a=np.array(["Apple", "Mango","Orange","Grapes","Jack Fruit"])
print(a)
print(a.size)

for i in range(0,a.size):
    print(a[i])

print("-----------------")
for j in a:
    print(j)