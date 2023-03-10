from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from core import models
from core import serializer
from core import permissions


class TraderTransactionAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TraderTransactionAPIList(generics.ListCreateAPIView):
    queryset = models.TraderTransaction.objects.all()
    serializer_class = serializer.TraderTransactionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = TraderTransactionAPIListPagination


class TraderTransactionAPTUpdate(generics.RetrieveUpdateAPIView):
    queryset = models.TraderTransaction.objects.all()
    serializer_class = serializer.TraderTransactionSerializer
    permission_classes = (IsAuthenticated,)


class TraderTransactionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.TraderTransaction.objects.all()
    serializer_class = serializer.TraderTransactionSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)

# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = models.Person.objects.all()
#     serializer_class = serializer.PersonSerializer
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = models.Category.objects.get(pk)
#         return Response({"cats": cats.name})


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
