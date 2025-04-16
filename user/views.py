from rest_framework.generics import CreateAPIView
from django.http.response import HttpResponse
from user.models import User
from user.serializers import UserSerializers

class CreateUserView(CreateAPIView):
    queryset = User
    serializer_class = UserSerializers

    