from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username")
    password = serializers.CharField(label="Password")

    def validate(self, value):
        username = value.get('username')
        password = value.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Xato: Natogri foydalanuvchi nomini kiritingiz'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = '"username" va "password" talab qilinadi.'
            raise serializers.ValidationError(msg, code='authorization')
        value['user'] = user
        return value
