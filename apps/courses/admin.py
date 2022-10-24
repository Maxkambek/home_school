from django.contrib import admin
from .models import StudentClass, StudentAge, Subject, CourseVideo, Theme

admin.site.register(Theme)
admin.site.register(StudentClass)
admin.site.register(StudentAge)
admin.site.register(Subject)
admin.site.register(CourseVideo)
