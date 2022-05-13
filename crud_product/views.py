from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response

class ProductList(generics.ListCreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request,  *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
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
            return Response({'status':'success','message':'Produk berhasil diubah', 'produk':serializer.data})
        return Response(serializer.errors, status=400)

    def destroy(self, request,  *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status':'success','message':'Produk berhasil dihapus'})
