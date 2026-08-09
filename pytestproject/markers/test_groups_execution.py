
import pytest

@pytest.mark.sanity
def test_scanity_testcase1():
    print("It is a First Sanity Testcase ")

@pytest.mark.sanity
def test_scanity_testcase2():
    print("It is a Second Sanity Testcase ")


@pytest.mark.api
def test_api_testcase1():
    print("It is a First API Testcase ")

@pytest.mark.api
def test_api_testcase2():
    print("It is a Second API Testcase ")

@pytest.mark.regression
def test_regression_testcase1():
    print("It is a First Regression Testcase ")

@pytest.mark.regression
def test_regression_testcase2():
    print("It is a Second Regression Testcase ")

@pytest.mark.database
def test_database_testcase1():
    print("It is a First Database Testcase ")

@pytest.mark.database
def test_database_testcase2():
    print("It is a Second Database Testcase ")