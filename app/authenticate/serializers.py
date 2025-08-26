from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     validators=[validate_password],
                                     min_length=8)

    password_2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('email', 'password', 'password_2', 'first_name', 'last_name', 'username')


    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return attrs


    def create(self, validated_data):
        validated_data.pop('password_2')

        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()