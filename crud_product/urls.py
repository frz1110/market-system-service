from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('market-product/', ProductList.as_view()),
    path('market-product/<int:pk>', ProductDetail.as_view()),
]
