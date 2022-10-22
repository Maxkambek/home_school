from .models import Subject, Theme, CourseVideo
from rest_framework.serializers import ModelSerializer


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'price']


class ThemeSerializer(ModelSerializer):
    subject_theme = SubjectSerializer()

    class Meta:
        model = Theme
        fields = ['id', 'name', 'subject_theme']


class CourseVideoSerializer(ModelSerializer):
    course_theme = ThemeSerializer

    class Meta:
        model = CourseVideo
        fields = ['id', 'name', 'description', 'course_theme', 'video']
