from rest_framework.serializers import ModelSerializer
from product.models import Product
from user.models import User

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']
        

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

     