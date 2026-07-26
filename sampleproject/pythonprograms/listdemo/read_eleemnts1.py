flowers=["Lotus","Sunflower", "Aster","Tulip","Jasmine","Lily"]

# When We need to use index appraoch of reading elements
# Taht object must support index
for i in range(0, len(flowers)):
    print(flowers[i])

print("-----------------")
j=0
while(j<len(flowers)):
    print(flowers[j])
    j=j+1

print("-----------------")
# IF you are not accessing teh Eleemnt based on index
for element in flowers:
    print(element)