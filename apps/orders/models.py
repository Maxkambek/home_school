import uuid
from django.db import models
from apps.accounts.models import Account
from apps.courses.models import Subject


class Order(models.Model):
    course = models.ForeignKey(Subject, on_delete=models.CASCADE)
    client = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_id = models.UUIDField(uuid.uuid4(), primary_key=True, editable=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class MyCourses(models.Model):
    course = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='my_courses')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name
