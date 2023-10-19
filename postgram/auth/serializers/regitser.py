from rest_framework import serializers

from postgram.user.serializers import UserSerializer
from postgram.user.models import User


class RegisterSerializer(UserSerializer):
    # Password that is at least 8 characters long and at most 128 characters and required
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User

        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'bio', 'avatar', 'is_active', 'created', 'updated',
                  'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
