from .models import Subject, Theme, CourseVideo, StudentClass, StudentAge
from rest_framework.serializers import ModelSerializer


class StudentClassSerializer(ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ['id', 'name']


class StudentAgeSerializer(ModelSerializer):
    class Meta:
        model = StudentAge
        fields = ['id', 'age']


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'price']


class ThemeSerializer(ModelSerializer):
    subject_theme = SubjectSerializer()

    class Meta:
        model = Theme
        fields = ['id', 'name', 'subject_theme', 'get_count']


class CourseVideoSerializer(ModelSerializer):
    courses_themes = ThemeSerializer()

    class Meta:
        model = CourseVideo
        fields = ['id', 'name', 'description', 'courses_themes', 'video']
