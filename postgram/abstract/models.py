from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
        except (ObjectDoesNotExist, TypeError, ValueError):
            return Http404
        else:
            return instance


class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid.uuid4)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = AbstractManager()

    class Meta:
        abstract = True
