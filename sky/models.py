from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Stuff (models.Model):
    title = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.title


class Package(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=1024)
    stuffs = models.ManyToManyField(Stuff)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    national_code = models.CharField(max_length=10, unique=True)
    is_supervisor = models.BooleanField(default=False)
    mobile = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now=True)
    packages = models.ManyToManyField(Package, through='PersonPackage')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PersonPackage(models.Model):
    DISTRIBUTING = 1
    DELIVERED = 2
    RETURNED = 3

    STATUS_CHOICES = [
        (DISTRIBUTING, 'Distributing'),
        (DELIVERED, 'Delivered'),
        (RETURNED, 'Returned'),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    distributor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,
                                      default=DISTRIBUTING)
