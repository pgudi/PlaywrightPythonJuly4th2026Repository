flowers=("Lotus","sunflower",100,10.44,True,False)
print(flowers)

# without using range function
for item in flowers:
    print(item)

print("-------------------")
# using range function
for i in range(0, len(flowers)):
    print(flowers[i])