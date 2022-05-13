from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class ProductList(generics.ListCreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
