from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from postgram.abstract.serializers import AbstractSerializer
from postgram.comment.models import Comment
from postgram.user.models import User
from postgram.post.models import Post
from postgram.user.serializers import UserSerializer


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        if self.context['request'].user != value:
            return ValidationError("You can't create a comment for another user.")

        return value

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        author = User.objects.get_object_by_public_id(rep['author'])

        rep['author'] = UserSerializer(author).data

        return rep

    class Meta:
        model = Comment

        fields = ['id', 'author', 'post', 'body', 'edited', 'created', 'updated']

        read_only_fields = ['edited']
