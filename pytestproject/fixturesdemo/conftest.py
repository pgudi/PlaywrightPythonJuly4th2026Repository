import pytest

@pytest.fixture(scope="function")
def setup():
    print("Launch Chrome Browser and Navigate Application URL !!!")
    yield
    print("Logout from the application and Close Chrome Browser")


@pytest.fixture(scope="class")
def class_setup():
    print("Launch Chrome Browser and Navigate Application URL - Class Level!!!")
    yield
    print("Logout from the application and Close Chrome Browser - Class Level")

@pytest.fixture(scope="module")
def module_setup():
    print("Launch Chrome Browser and Navigate Application URL - Module Level!!!")
    yield
    print("Logout from the application and Close Chrome Browser - Module Level")