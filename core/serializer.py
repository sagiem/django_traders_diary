import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from core import models


# class PersonModel:
#     def __init__(self, login, email):
#         self.login = login
#         self.email = email


class PersonSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=255)
    name = serializers.CharField()
    surName = serializers.CharField()
    patronymic = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()
    registerData = serializers.DateTimeField(read_only=True)
    catPerson = serializers.IntegerField()


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