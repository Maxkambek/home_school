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


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=14)
    password = serializers.CharField(max_length=100)


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=64, write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = Account
        fields = ['password', 'old_password']

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        password = attrs.get('password')
        request = self.context.get('request')
        try:
            user = request.user
        except:
            raise serializers.ValidationError({'message': 'User not found'})

        if not user.check_password(old_password):
            raise serializers.ValidationError({'message': 'Old password not match'})

        user.set_password(password)
        user.save()
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'phone', 'first_name', 'last_name']
