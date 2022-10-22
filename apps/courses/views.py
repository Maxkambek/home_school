from .serializers import CourseVideoSerializer, SubjectSerializer, ThemeSerializer
from .models import Theme, Subject, CourseVideo
from rest_framework import generics
from apps.orders.models import MyCourses
from apps.orders.serializers import MyCoursesSerializer


class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ThemeListAPIView(generics.ListAPIView):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        queryset = Theme.objects.all()
        pk = self.request.GET.get('subject')
        if pk:
            queryset = queryset.filter(subject_id=pk)
        return queryset


class CourseVideoListAPIView(generics.ListAPIView):
    serializer_class = CourseVideoSerializer

    def get_queryset(self):
        queryset = CourseVideo.objects.all()
        pk = self.request.GET.get('theme')
        if pk:
            queryset = queryset.filter(theme_id=pk)
        return queryset


class MyCoursesAPIView(generics.ListAPIView):
    serializer_class = MyCoursesSerializer
    queryset = MyCourses.objects.all()
