
def is_prime(num):
    flag=0
    for i in range(2,num):
        if(num % i ==0):
            flag=flag+1
            break

    if(flag==0):
        return True
    else:
        return False

# Verify the number prime or not
v1=is_prime(21)
print(v1)
print("------------------------")
# Display Prime numebrs in between 1 to 50
for i in range(1,51):
    if(is_prime(i)==True):
        print(i, end= " ")

print()
print("------------------------")
# Display sum of Prime numebrs in between 1 to 100
sum=0
for i in range(1,51):
    if(is_prime(i)==True):
        sum=sum+i

print()
print("sum of Prime Numbers :",sum)

print("------------------------")
# Display Count of Prime numebrs in between 100 to 200
count=0
for i in range(100,201):
    if(is_prime(i)==True):
        count=count+1

print()
print("Count of Prime Numbers :",count)

print("------------------------")