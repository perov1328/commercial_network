from products.apps import ProductsConfig
from django.urls import path
from products.api_views import (ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView,
                                ProductDeleteAPIView, ProductUpdateAPIView)

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product_list'),
    path('create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
]
