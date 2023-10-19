import pytest

from postgram.comment.models import Comment
from postgram.fixtures.user import user
from postgram.fixtures.post import post


@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")
