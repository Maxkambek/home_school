from .serializers import CourseVideoSerializer, SubjectSerializer, ThemeSerializer, StudentClassSerializer, \
    StudentAgeSerializer
from .models import Theme, Subject, CourseVideo, StudentClass, StudentAge
from rest_framework import generics
from apps.orders.models import MyCourses
from apps.orders.serializers import MyCoursesSerializer


class StudentClassListAPIView(generics.ListAPIView):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer


class StudentAgeListAPIView(generics.ListAPIView):
    queryset = StudentAge.objects.all()
    serializer_class = StudentAgeSerializer


class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ThemeListAPIView(generics.ListAPIView):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        queryset = Theme.objects.all()
        pk = self.request.GET.get('subject_id')
        if pk:
            queryset = queryset.filter(subject_id=pk)
        return queryset


class CourseVideoListAPIView(generics.ListAPIView):
    serializer_class = CourseVideoSerializer

    def get_queryset(self):
        queryset = CourseVideo.objects.all()
        pk = self.request.GET.get('theme_id')
        if pk:
            queryset = queryset.filter(theme_id=pk)
        return queryset


class MyCoursesAPIView(generics.ListAPIView):
    serializer_class = MyCoursesSerializer
    queryset = MyCourses.objects.all()
