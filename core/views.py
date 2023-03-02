from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from core import models
from core import serializer
from rest_framework.views import APIView


class PersonAPIView(APIView):
    def get(self, reguest):
        lst = models.Person.objects.all()
        return  Response({'person': serializer.PersonSerializer(lst, many=True).data})
    def post(self, request):
        serializers = serializer.PersonSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        post_new = models.Person.objects.create(
            login=request.data['login'],
            name=request.data['name'],
            surName=request.data['surName'],
            patronymic=request.data['patronymic'],
            email=request.data['email'],
            phone=request.data['phone'],
            catPerson_id=request.data['catPerson_id']
        )
        return Response({'person': serializer.PersonSerializer(post_new).data})

# class PersonAPIView(generics.ListAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializer.PersonSerializer



