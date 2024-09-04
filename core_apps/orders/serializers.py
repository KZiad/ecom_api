from rest_framework import serializers
from .models import Order, Order_Item
from core_apps.products.models import Product
from core_apps.products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        return obj.total

    class Meta:
        model = Order_Item
        fields = ['product_name', 'product_price',
                  'product_quantity', 'total', 'product']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        return obj.user.id

    def get_total(self, obj):
        return obj.total

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'created_at', 'total', 'items']
        read_only_fields = ['id', 'user_id', 'created_at', 'total', 'items']
