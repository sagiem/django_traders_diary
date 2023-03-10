# Generated by Django 4.1.7 on 2023-03-06 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Финансовый инструмент')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('surName', models.CharField(max_length=255)),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('registerData', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TraderTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataOpen', models.DateField(verbose_name='Дата открытия')),
                ('timeOpen', models.TimeField(verbose_name='Время открытия')),
                ('dataClosing', models.DateField(verbose_name='Дата закрытия')),
                ('timeClosing', models.TimeField(verbose_name='Время закрытия')),
                ('transDir', models.CharField(max_length=10, verbose_name='Направление сделки')),
                ('priceOpen', models.CharField(max_length=50, verbose_name='Цена открытия')),
                ('priceClosing', models.CharField(max_length=50, verbose_name='Цена закрытия')),
                ('volume', models.CharField(max_length=50, verbose_name='Объем')),
                ('finTools', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.financetools')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.person')),
            ],
        ),
    ]
