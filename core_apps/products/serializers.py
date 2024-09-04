from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'price']
