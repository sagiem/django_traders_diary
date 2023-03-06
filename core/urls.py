from django.urls import path, include
from core import views
from rest_framework import routers

#
# router = routers.DefaultRouter()
# router.register(r'core', views.PersonViewSet)
# print(router.urls)


urlpatterns = [
    # path('api/v1/', include(router.urls))
    # path('api/v1/personlist/', views.PersonViewSet.as_view({'get': 'list'})),
    # path('api/v1/personlist/<int:pk>', views.PersonViewSet.as_view({'put': 'update'}))
    # path('api/v1/drf-auth', include('rest_framework.utils')),
    path('api/v1/TraderTransaction', views.TraderTransactionAPIList.as_view()),
    path('api/v1/TraderTransaction/<int:pk>', views.TraderTransactionAPTUpdate.as_view()),
    path('api/v1/TraderTransactionDelete/<int:pk>', views.TraderTransactionAPIDestroy.as_view())
]