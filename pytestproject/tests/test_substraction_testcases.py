from sourcecode.basicmaths import substraction

def test_positive_numbers():
    num1=40
    num2=15
    assert substraction(num1,num2)==25

def test_negative_numbers():
    num1=-50
    num2=-100
    assert substraction(num1,num2)==50

def test_positive_negative_numbers():
    num1=-50
    num2=120
    assert substraction(num1,num2)==-170

