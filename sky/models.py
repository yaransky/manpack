from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10, unique=True)
    is_supervisor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Stuff (models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    stuffs = models.ForeignKey(Stuff, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
