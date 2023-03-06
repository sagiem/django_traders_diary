from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    login = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    surName = models.CharField(max_length=255, null=False)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=50, blank=False)
    # phone = PhoneNumberField(unique=True, null=False, blank=False)
    registerData = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.login


class TraderTransaction(models.Model):
    dataOpen = models.DateField('Дата открытия',)
    timeOpen= models.TimeField('Время открытия')
    dataClosing = models.DateField('Дата закрытия',)
    timeClosing = models.TimeField('Время закрытия')
    finTools = models.ForeignKey('FinanceTools', on_delete=models.PROTECT, null=True)
    transDir = models.CharField('Направление сделки',max_length=10)
    priceOpen = models.CharField('Цена открытия', max_length=50)
    priceClosing = models.CharField('Цена закрытия', max_length=50)
    volume = models.CharField('Объем', max_length=50)
    user = models.ForeignKey('Person', on_delete=models.PROTECT, null=True)


class FinanceTools(models.Model):
    name =models.CharField('Финансовый инструмент', max_length=50)

    def __str__(self):
        return self.name




