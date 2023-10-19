import pytest

from postgram.comment.models import Comment
from postgram.fixtures.user import user
from postgram.fixtures.post import post


@pytest.mark.django_db
def test_create_comment(user, post):
    post_comment = Comment.objects.create(author=user, post=post, body="Test Comment Body")
    assert post_comment.body == "Test Comment Body"
    assert post_comment.author == user


