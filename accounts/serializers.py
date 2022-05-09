from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_username(self, value):
        if value.lower() == 'admin':
            raise serializers.ValidationError('Username cannot be admin')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        return data

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
