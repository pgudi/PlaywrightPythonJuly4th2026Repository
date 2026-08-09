from sourcecode.basicmaths import addition

def test_positive_numbers():
    num1=30
    num2=40
    assert addition(num1,num2) == 70

def test_negative_numbers():
    num1=-50
    num2=-100
    assert addition(num1, num2) == -150

def test_positive_negative_numbers():
    num1=-50
    num2=120
    assert addition(num1, num2) ==70