from django.urls import path
from core import views

urlpatterns = [
    path('api/v1/personlist', views.PersonAPIView.as_view())
]