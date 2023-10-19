from postgram.user.models import User
from postgram.abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'bio', 'avatar', 'created', 'updated', 'is_active']

        read_only_fields = ['is_active']

