from rest_framework import serializers
from ..models import Category, City, Product,ProductImage
from accounts.api.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = City
        fields = '__all__'
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ['product']

class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    city = CitySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source='category',
        write_only= True 
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city',
        write_only = True 
    )

    class Meta : 
        model = Product
        fields = '__all__'
        
    def validate_price(self,value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value