from django.shortcuts import render
from ..models import Product,Category, City 
from rest_framework import status,generics,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer,CategorySerializer, CitySerializer


# Product 
class ProductAV(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

# Product Detail
class ProductDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# List Products by Category 
class ProductListByCategoryAV(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id = category_id)

# List Products by City 
class ProductListByCityAV(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Product.objects.filter(city_id=city_id)

# List Categories 
class CategoryListAV(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# List Cities 
class CityListAV(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
