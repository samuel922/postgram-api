import pytest

from rest_framework import status

from postgram.fixtures.user import user


class TestAuthViewSets:

    endpoint = "/api/auth/"

    def test_login(self, client, user):
        data = {
            "email": user.email,
            "password": "test_password"
        }

        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
        assert response.data['user']['id'] == user.public_id.hex
        assert response.data['user']['username'] == user.username
        assert response.data['user']['email'] == user.email

    def test_register(self, client, user):
        data = {
            "username": "test_username",
            "email": "email@gmail.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "test_password"
        }

        response = client.post(self.endpoint + "register/", data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_refresh(self, client, user):
        data = {
            "email": user.email,
            "password": "test_password"
        }
        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK

        data_refresh = {
            "refresh": response.data["refresh"]
        }

        response = client.post(self.endpoint + "refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
