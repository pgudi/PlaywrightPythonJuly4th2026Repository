import pytest

def test_validate_number():
    x=40
    y=30
    assert (x + y) ==70

def test_lessthan_validation():
    x=150
    assert (100 < x) == True

def test_greaterthan_validation():
    a=450
    assert (750 > a) ==True

def test_existance_validation():
    str1="Welcome"
    str2="Every Welcome to Office"
    assert str1 in str2

def test_existance_validation2():
    str1="Programming"
    str2="Java Programming Language"
    assert (str1 in str2)

def test_reference_validation1():
    str1="Programming"
    str2="Java Programming Language"
    assert str1 is not str2

def test_reference_validation2():
    str1="Programming"
    str2="Programming"
    assert str1 is str2