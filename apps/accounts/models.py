from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from apps.courses.models import StudentClass, StudentAge

SEX = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

USER_TYPE = (
    (1, 'Parent'),
    (2, 'Student')
)


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **extra_fields)
        user.is_verified = True
        user.is_staff = True
        user.is_parent = True
        user.is_superuser = True
        # user.is_teacher = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_parent = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    parent_id = models.PositiveIntegerField(default=0)
    student_id = models.PositiveIntegerField(default=0)
    sex = models.CharField(choices=SEX, max_length=12, default='Male')
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, default='2')
    age = models.ForeignKey(StudentAge, on_delete=models.SET_NULL, null=True, blank=True)
    date_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = ("Telefon raqamni tasdiqlash")
        verbose_name_plural = ("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")
    code = models.CharField(max_length=10, verbose_name="Kod")
