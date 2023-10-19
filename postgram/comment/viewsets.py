from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from postgram.abstract.viewsets import AbstractViewSet
from postgram.auth.permissions import UserPermission
from postgram.comment.models import Comment
from postgram.comment.serializers import CommentSerializer


class CommentViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        post_pk = self.kwargs['post_pk']
        if post_pk is None:
            return Http404

        return Comment.objects.filter(post__public_id=post_pk)

    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
