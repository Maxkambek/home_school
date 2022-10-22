from .models import Order, MyCourses
from rest_framework import serializers
from apps.courses.serializers import SubjectSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'course', 'client']


class MyCoursesSerializer(serializers.ModelSerializer):
    my_courses = SubjectSerializer()

    class Meta:
        model = MyCourses
        fields = ['id', 'my_courses', 'user']
