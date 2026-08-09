import pytest

@pytest.mark.parametrize(
    "num1, num2, result",
    [(10,20,30), (25,50, 75), (4, 6 ,10)]
)

def test_add_parametrize(num1, num2, result):
    assert (num1 + num2) == result
