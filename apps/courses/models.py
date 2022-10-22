from django.db import models


class StudentClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student Class'
        verbose_name_plural = 'Student Classes'


class StudentAge(models.Model):
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.age

    class Meta:
        verbose_name = 'Student Age'
        verbose_name_plural = 'Student Age'


class Subject(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='subjects/', null=True, blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Theme(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'


class CourseVideo(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='course_video')
    name = models.CharField(max_length=221)
    description = models.TextField()
    video = models.FileField(upload_to=f'{theme.name}')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course Video'
        verbose_name_plural = 'Course Videos'
