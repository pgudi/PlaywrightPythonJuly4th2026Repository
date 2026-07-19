
# num=10

# def display_numbers():
#     global num

#     if(num<=20):
#         print(num)
#         num=num+1
#         display_numbers()

# display_numbers()

print("--------------------------")
# Even number in between 20 to 40
number=20
def display_even_number():
    global number
    if(number <=40):
        if(number % 2 ==0):
            print(number)
            
        number=number+1
        display_even_number()

display_even_number()


