import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from core import models


# class PersonModel:
#     def __init__(self, login, email):
#         self.login = login
#         self.email = email


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields =("__all__")

class TraderTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = models.TraderTransaction
        fields = ("__all__")

# class PersonSerializer(serializers.Serializer):
#     login = serializers.CharField(max_length=255)
#     name = serializers.CharField()
#     surName = serializers.CharField()
#     patronymic = serializers.CharField()
#     email = serializers.CharField()
#     phone = serializers.CharField()
#     registerData = serializers.DateTimeField(read_only=True)
#     catPerson_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return models.Person.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.login = validated_data.get("login", instance.login)
#         instance.name = validated_data.get("name", instance.name)
#         instance.surName = validated_data.get("surName", instance.surName)
#         instance.patronymic = validated_data.get("patronymic)", instance.patronymic)
#         instance.email = validated_data.get("email", instance.email)
#         instance.phone = validated_data.get("phone", instance.phone)
#         instance.registerData = validated_data.get("registerData", instance.registerData)
#         instance.catPerson_id = validated_data.get("catPerson_id", instance.catPerson_id)
#         instance.save()
#         return instance


# def encode():
#     model = PersonModel('max', 'max@yandex.ru')
#     model_sr = PersonSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     steam = io.BytesIO(b'{"login":"max","email":"max@yandex.ru"}')
#     data = JSONParser().parse(steam)
#     serializer = PersonSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)