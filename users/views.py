from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.generics import CreateAPIView

from .serializers import LoginSerializer, SignupSerializer
# Create your views here.


class LoginView(APIView):
    """
    Endpoint for login you need to enter your username and password
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response('Muvafaqiiyatli otdingiz')


class Signup(CreateAPIView):
    """
    Endpoint for signup.You need to enter the username and password
    """
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
