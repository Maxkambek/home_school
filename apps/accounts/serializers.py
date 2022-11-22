from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Account, VerifyPhone


class RegisterParentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = Account
        fields = ['id', 'phone', 'password']


class RegisterStudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = Account
        fields = ['id', 'phone', 'first_name', 'last_name', 'password', 'sex', 'student_class', 'age']


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Account
        fields = ['phone']


class VerifyRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)

    class Meta:
        model = VerifyPhone
        fields = ['phone', 'code', 'password']


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name']
