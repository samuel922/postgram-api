from rest_framework import status

from postgram.fixtures.user import user
from postgram.fixtures.post import post


class TestPostViewSet:
    endpoint = "/api/post/"

    def test_list(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_retrieve(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.public_id) + "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == post.public_id.hex
        assert response.data['author']['id'] == post.author.public_id.hex
        assert response.data['body'] == post.body

    def test_update(self, client, user, post):
        client.force_authenticate(user=user)
        data = {
            "body": "Test Post Body Update",
            "author": user.public_id.hex
        }
        response = client.put(self.endpoint + str(post.public_id) + "/", data)
        assert response.status_code == status.HTTP_200_OK

    def test_delete(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint + str(post.public_id) + "/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_list_anonymous(self, client, post):
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve_anonymous(self, client, post):
        response = client.get(self.endpoint + str(post.public_id) + "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['body'] == post.body
        assert response.data['author']['id'] == post.author.public_id.hex

    def test_create_anonymous(self, client, post):
        data = {}
        response = client.post(self.endpoint + str(post.public_id) + "/", data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_anonymous(self, client, post):
        data = {}
        response = client.put(self.endpoint + str(post.public_id) + "/", data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_anonymous(self, client, post):
        response = client.delete(self.endpoint + str(post.public_id) + "/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
