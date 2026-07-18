# Programmatically add result of 9th table in to a list and find sum of all elements
'''
  Step 1: Make sure you print numbers 1 t o10
  Step 2: Make sure you can multiple 9 with numbers 1 to 10 and print result
  Step 3: Declare an list
  Step 4: Add Elements (result of 9th table)
  Step 5: Find sum of All Elements from list
'''
result=[]

for i in range(1 , 11):
    result.append(i * 9)

sum=0
for i in range(0, len(result)):
    sum=sum + result[i]

print("Sum Result :",sum)

print("---------------------------------")
# apply list comprenhsive 
sumresult=0
result2= [x for x in range(1,91) if (x % 9 ==0)] 
print(result2)
sum1=0
for i in range(0, len(result2)):
    sum1=sum1 + result2[i]
print(sum1)