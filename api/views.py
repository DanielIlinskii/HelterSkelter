import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import User, AccessLevel
from .serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    filter_users = (
        User.objects
        .filter(
            access_level=AccessLevel.ADMIN,
        )
        .order_by('-date_of_birth')
    )

    return Response(serializer.data)
