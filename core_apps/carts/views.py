from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, status
from .models import Cart_Item, Cart
from core_apps.products.models import Product
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CartItemSerializer, CartSerializer


class CartViewSet(viewsets.GenericViewSet):
    queryset = Cart_Item.objects.select_related('cart', 'product')
    permission_classes = [IsAuthenticated,]
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)

    def create(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = Cart_Item.objects.get_or_create(
            cart=cart, product=product)
        if not created:
            item.quantity += 1
        item.save()
        return Response(self.get_serializer(cart).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item = get_object_or_404(
            Cart_Item, product__pk=kwargs.get('pk'), cart=cart)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        return Response(self.get_serializer(cart).data)

    def list(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return Response(self.get_serializer(cart).data)
