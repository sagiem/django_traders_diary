# Generated by Django 4.1.7 on 2023-03-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='patronymic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
