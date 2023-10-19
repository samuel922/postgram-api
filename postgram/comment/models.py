from django.db import models

from postgram.abstract.models import AbstractModel, AbstractManager


# Create your models here.
class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    author = models.ForeignKey(to="postgram_user.User", on_delete=models.CASCADE)
    post = models.ForeignKey(to="postgram_post.Post", on_delete=models.CASCADE)

    body = models.TextField()

    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return f"{self.author.name}"
