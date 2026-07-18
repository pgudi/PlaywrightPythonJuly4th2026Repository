# declare and assign items
flowers=["Sunflower","Cosmos","Tulip",True, 200,10.45,"Cosmos","Cosmos"]
print(flowers)

# append : adding Element
flowers.append("Jack Fruit")
print(flowers)

# Insert Element
flowers.insert(0,"Rose")
print(flowers)

# Remove Element
flowers.remove("Rose")
print(flowers)

# pop It removes last element
flowers.pop()
print(flowers)

# How to add New list in Existing lsit 
numbers=[10,20,30,40]
flowers.extend(numbers)
print(flowers)

# index it provides index based on given element
v1=flowers.index("Cosmos")
print(v1)

#reverse
flowers.reverse()
print(flowers)

# count it provides Element count
v2=flowers.count("Cosmos")
print(v2)

# sort Elements
fruits=[40,10,80,30,60]
fruits.sort()
print(fruits)

# copy 
test=flowers.copy()
print(test)