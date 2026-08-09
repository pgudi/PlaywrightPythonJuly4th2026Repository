import pytest

@pytest.mark.parametrize(
    "username, password",
    [("admin","admin123"), ("developer1","developer123"),("user1","user123")]
)

def test_login_parametrize(username, password):
    print(username , "->" , password)