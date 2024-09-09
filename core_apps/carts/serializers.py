from rest_framework import serializers
from .models import Cart_Item, Cart
from core_apps.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    quantity = serializers.IntegerField

    def get_product(self, obj):
        return ProductSerializer(obj.product).data

    class Meta:
        model = Cart_Item
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    items = CartItemSerializer(many=True)

    def get_total(self, obj):
        return obj.total

    def get_user_id(self, obj):
        return obj.user.id

    class Meta:
        model = Cart
        fields = ['user_id', 'total', 'items']
        read_only_fields = ['user_id', 'total', 'items']
