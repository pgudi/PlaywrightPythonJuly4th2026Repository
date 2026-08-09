import pytest

@pytest.mark.skip
def test_first_testcase():
    print("It is a First Testcase")

def test_second_testcase():
    print("It is a Second Testcase")

def test_third_testcase():
    print("It is a Third Testcase")

@pytest.mark.skip
def test_fourth_testcase():
    print("It is a Fourth Testcase")

def test_fifth_testcase():
    print("It is a Fifth  Testcase")

def test_sixth_testcase():
    print("It is a Sixth Testcase")

def test_seventh_testcase():
    print("It is a Seventh Testcase")

@pytest.mark.xfail
def test_eighth_testcase():
    print("It is a Eighth Testcase")
    assert (10 < 5) ==True