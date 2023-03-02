from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    login = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    surName = models.CharField(max_length=255, null=False)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=50, blank=False)
    # phone = PhoneNumberField(unique=True, null=False, blank=False)
    registerData = models.DateTimeField(auto_now_add=True)
    catPerson = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.login


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
