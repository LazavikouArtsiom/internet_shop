from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.is_active = True
        user.is_admin = False
        user.is_staff = False

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffruser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_active = True
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email



class Profile(models.Model):
    SEXES = (
        ('Male','Мужчина'),
        ('Femaie','Женщина')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True, verbose_name='Адрес доставки')
    sex = models.CharField(max_length=20, choices=SEXES, blank=True, verbose_name='Пол')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __str__(self):
        return self.user.email + ' ' + self.full_name