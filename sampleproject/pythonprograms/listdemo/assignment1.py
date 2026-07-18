# Programmatically add even numbers 30 to 50 in to a list and read Elements in reverse order.?
'''
step 1: make sure you can print numebrs 30 to 50
Step 2: Make sure you can print even number in between 30 to 50
Step 3: Declare a list
Step 4: append /add Even numebrs into list
Step 5: REad Elements in Reverse order

'''
even =[]
for i in range(30,51):
    if(i % 2 ==0):
        even.append(i)

print(even)

# display in Reverse
even.reverse()
print(even)

print("--------------------------------------")
even1=[x for x in range(30,51) if (x % 2 ==0)]
even1.reverse()
print(even1)
