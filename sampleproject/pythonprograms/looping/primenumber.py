
flag=0
num=17

for i in range(2, num):
    if( num % i ==0):
        flag=flag+1
        break

if(flag==0):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
