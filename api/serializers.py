from rest_framework import serializers
from .models import NewsData


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        fields = ['title', 'content', 'link']
