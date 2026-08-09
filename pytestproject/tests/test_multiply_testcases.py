from sourcecode.basicmaths import multiply

def test_positive_number():
    num1=12
    num2=10
    assert multiply(num1,num2)==120

def test_negative_numbers():
    num1=-15
    num2=-20
    assert multiply(num1,num2)==300

def test_positive_negative():
    num1=25
    num2=-25
    assert multiply(num1,num2)==-625

    