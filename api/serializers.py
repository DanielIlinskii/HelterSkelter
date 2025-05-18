from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    adress = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'address': {'read_only': True},
        }


