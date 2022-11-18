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
    class_subject = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def general_price(self):
        prices = self.subject_theme.all()
        return sum([i.get_price for i in prices])

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Theme(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_theme')
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.courses_themes.count()

    @property
    def get_price(self):
        courses = self.courses_themes.all()
        return sum([i.price for i in courses])

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'


class CourseVideo(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='courses_themes')
    name = models.CharField(max_length=221)
    description = models.TextField()
    video = models.FileField(upload_to=f'{theme.name}')
    price = models.PositiveIntegerField(default=50000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course Video'
        verbose_name_plural = 'Course Videos'
