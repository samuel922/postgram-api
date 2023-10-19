from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from postgram.abstract.models import AbstractModel, AbstractManager


# Create your models here.
class UserManager(AbstractManager, BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """Return a user with a username, email, password, phone number ..."""
        if username is None:
            raise TypeError("Users must have a password")
        if email is None:
            raise TypeError("Users must have an email.")
        if password is None:
            raise TypeError("Users must have a password")

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        """Create and return a user with admin rights"""
        if username is None:
            raise TypeError("Superusers must have a username.")
        if email is None:
            raise TypeError("Superusers must have an email.")
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(db_index=True, unique=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)

    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)

    posts_liked = models.ManyToManyField("postgram_post.Post", related_name="liked_by")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def like(self, post):
        return self.posts_liked.add(post)

    def remove_like(self, post):
        return self.posts_liked.remove(post)

    def has_liked(self, post):
        return self.posts_liked.filter(pk=post.pk).exists()
