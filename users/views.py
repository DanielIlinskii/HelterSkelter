from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .schemas import UserCreate, UserResponse
from .database import get_db
from sqlalchemy.orm import Session
from django.http import HttpRequest, HttpResponse


class UserListCreateView(APIView):
    def get(self, request):
        db: Session = get_db().__next__()
        users = db.query(User).all()
        return Response([UserResponse.from_orm(user).dict() for user in users])

    def post(self, request):
        data = UserCreate(**request.data)
        db: Session = get_db().__next__()
        new_user = User(**data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return Response(
            UserResponse.from_orm(new_user).dict(), status=status.HTTP_201_CREATED
        )


def test(request):
    return HttpResponse("test")
