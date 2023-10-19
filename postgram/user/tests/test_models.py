import pytest

from postgram.user.models import User

data = {
    "first_name": "Test",
    "last_name": "User",
    "username": "test_username",
    "email": "test@email.com",
    "password": "test_password"
}

data_superuser = {
    "first_name": "Super",
    "last_name": "User",
    "username": "test_super_user",
    "email": "superuser@gmail.com",
    "password": "test_password"
}


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**data)
    assert user.first_name == data['first_name']
    assert user.last_name == data['last_name']
    assert user.username == data['username']
    assert user.email == data['email']


@pytest.mark.django_db
def test_superuser():
    user = User.objects.create_superuser(**data_superuser)
    assert user.first_name == data_superuser['first_name']
    assert user.last_name == data_superuser['last_name']
    assert user.username == data_superuser['username']
    assert user.email == data_superuser['email']
    assert user.is_superuser == True
    assert user.is_staff == True
