from rest_framework import serializers
from product.models import Product, Aggregate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = '__all__'