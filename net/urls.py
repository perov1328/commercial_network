from net.apps import NetConfig
from django.urls import path
from net.api_views import (NetElementListAPIView, NetElementCreateAPIView, NetElementRetriveAPIView,
                           NetElementDeleteAPIView, NetElementUpdateAPIView)

app_name = NetConfig.name

urlpatterns = [
    path('', NetElementListAPIView.as_view(), name='net_list'),
    path('create/', NetElementCreateAPIView.as_view(), name='net_create'),
    path('<int:pk>/', NetElementRetriveAPIView.as_view(), name='net_retrieve'),
    path('<int:pk>/delete/', NetElementDeleteAPIView.as_view(), name='net_delete'),
    path('<int:pk>/update/', NetElementUpdateAPIView.as_view(), name='net_update'),
]
