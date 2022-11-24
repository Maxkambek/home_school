from django.contrib import admin
from .models import StudentClass, StudentAge, Subject, CourseVideo, Theme
from modeltranslation.admin import TranslationAdmin


class StudentClassAdmin(TranslationAdmin):
    list_display = ['name', 'id']


class StudentAgeAdmin(TranslationAdmin):
    list_display = ['age', 'id']


class SubjectAdmin(TranslationAdmin):
    list_display = ['name', 'class_subject']


class ThemeAdmin(TranslationAdmin):
    list_display = ['name', 'subject']


class CourseVideoAdmin(TranslationAdmin):
    list_display = ['name', 'theme']


admin.site.register(Theme)
admin.site.register(StudentClass)
admin.site.register(StudentAge)
admin.site.register(Subject)
admin.site.register(CourseVideo)
