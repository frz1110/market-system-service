from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
 
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer


    def get_queryset(self):
        if 'product' in cache:
            print('cache')
            return cache.get('product')
        else:
            print('nocache')
            result = Product.objects.all()
            cache.set('product', result, 300)
            return result

    def create(self, request,  *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            if 'product' in cache:
                cache.delete('product')

            return Response({'status':'success','message':'Produk berhasil dibuat', 'produk':serializer.data},
                             status=201)
        return Response(serializer.errors, status=400)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()

    def update(self, request,  *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

            if 'product' in cache:
                cache.delete('product')

            return Response({'status':'success','message':'Produk berhasil diubah', 'produk':serializer.data})
        return Response(serializer.errors, status=400)

    def destroy(self, request,  *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        if 'product' in cache:
            cache.delete('product')
        return Response({'status':'success','message':'Produk berhasil dihapus'})
