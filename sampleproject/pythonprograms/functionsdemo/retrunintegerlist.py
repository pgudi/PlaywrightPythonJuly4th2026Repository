def get_integer_list():
    numbers = [10,20,30,40,50,60]
    return numbers

# display elements from return value
v1=get_integer_list()
print(v1)
print("--------------")
# find sum of Elements in a list
sum=0
for i in range(0, int(len(v1))):
    sum=sum+v1[i]
print("Sum of eleemnts :",sum)
print("--------------")
# print First Half of teh Elements

for i in range(0, len(v1)//2):
    print(v1[i])

print("--------------")
# print Second Half of teh Elements

for i in range((len(v1)//2), len(v1)):
    print(v1[i])
