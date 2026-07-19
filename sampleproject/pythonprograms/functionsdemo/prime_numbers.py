
def display_prime_numbers():
    for num in range(50,101):
        flag=0
        for i in range(2, num):
            if(num % i ==0):
                flag=flag+1
                break
        if(flag==0):
            print(num, end=" ")

display_prime_numbers()