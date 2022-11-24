from modeltranslation.translator import register, TranslationOptions
from .models import StudentClass, StudentAge, Subject, Theme, CourseVideo


@register(StudentClass)
class StudentClassTrans(TranslationOptions):
    fields = ('name',)


@register(StudentAge)
class StudentAgeTrans(TranslationOptions):
    fields = ('age',)


@register(Subject)
class SubjectTrans(TranslationOptions):
    fields = ('name',)


@register(Theme)
class ThemeTrans(TranslationOptions):
    fields = ('name',)


@register(CourseVideo)
class VideoTrans(TranslationOptions):
    fields = ('name', 'description')
