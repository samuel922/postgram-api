from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from postgram.abstract.viewsets import AbstractViewSet
from postgram.user.serializers import UserSerializer
from postgram.user.models import User


class UserViewSet(AbstractViewSet, viewsets.ModelViewSet):
    http_method_names = ['patch', 'get']
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
