from rest_framework import generics
import requests
from bs4 import BeautifulSoup

from .models import NewsData
from .serializers import NewsSerializer
# Create your views here.
