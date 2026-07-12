evensum=0
oddsum=0

for i in range(1,501):
    if(i % 2 ==0):
        evensum=evensum + i
    else:
        oddsum=oddsum + i

print("Sum of Even Number :",evensum)
print("Sum of Odd Number :",oddsum)