import pytest

from postgram.user.models import User

data = {
    "first_name": "User",
    "last_name": "Test",
    "username": "user_test",
    "email": "user@email.com",
    "password": "test_password"
}


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data)
