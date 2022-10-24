from django.urls import path
from . import views

urlpatterns = [
    path('list-subject/', views.SubjectListAPIView.as_view()),
    path('list-themes/', views.ThemeListAPIView.as_view()),
    path('list-videos/', views.CourseVideoListAPIView.as_view()),
    path('list-mycourses/', views.MyCoursesAPIView.as_view()),
    path('list-classes/', views.StudentClassListAPIView.as_view()),
    path('list-ages/', views.StudentAgeListAPIView.as_view())
]
