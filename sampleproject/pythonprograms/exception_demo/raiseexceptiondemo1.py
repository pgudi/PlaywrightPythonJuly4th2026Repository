# Verify teh given number is Positive

def verify_positive_number(num):
    try:
        if(num<0):
            raise Exception("If any number less than Zero, It is a Negative Number")
        else:
            print("It is a Positive Number")
    except Exception as e:
        print("Exception :", e)


verify_positive_number(50)
verify_positive_number(-11)
