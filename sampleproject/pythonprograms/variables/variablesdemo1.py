# sum=0
# for i in range(1, 11):
#     sum=sum+i

# print("sum of Numbers in between 1 to 10 :", sum)
sum=0
def find_sum():
    global sum
    for i in range(1,11):
        sum = sum +i

    print("sum of Numbers in between 1 to 10 :",sum)

find_sum()