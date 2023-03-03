from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from core import models
from core import serializer
from rest_framework.views import APIView


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializer.PersonSerializer




# class PersonAPIList(generics.ListCreateAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializer.PersonSerializer
#
#
# class PersonAPIUpdate(generics.UpdateAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializer.PersonSerializer
#
# class PersonAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializer.PersonSerializer
