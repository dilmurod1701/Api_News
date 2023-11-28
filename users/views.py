from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.generics import CreateAPIView

from .serializers import LoginSerializer, SignupSerializer
# Create your views here.
