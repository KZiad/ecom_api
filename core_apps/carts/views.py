from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from .models import Cart_Item, Cart
from core_apps.products.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CartSerializer
from drf_yasg.utils import swagger_auto_schema, no_body


class CartViewSet(viewsets.GenericViewSet):
    queryset = Cart_Item.objects.select_related('cart', 'product')
    permission_classes = [IsAuthenticated,]
    serializer_class = CartSerializer

    def get_queryset(self):

        # To fix a warning that happens when swagger tries to generate the schema
        if self.request.user.is_anonymous:
            return Cart_Item.objects.none()

        return self.queryset.filter(cart__user=self.request.user)

    @swagger_auto_schema(operation_summary='Add a product to the cart, \
                         or increase quantity by 1',
                         responses={201: CartSerializer()},
                         request_body=no_body)
    def create(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = Cart_Item.objects.get_or_create(
            cart=cart, product=product)
        if not created:
            item.quantity += 1
        item.save()
        return Response(self.get_serializer(cart).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_summary='Remove a product to the cart, \
                         or decrease quantity by 1',
                         responses={204: CartSerializer()})
    def destroy(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item = get_object_or_404(
            Cart_Item, product__pk=kwargs.get('pk'), cart=cart)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        return Response(self.get_serializer(cart).data, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(operation_summary="List all products in the user's cart",
                         responses={200: CartSerializer()})
    def list(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return Response(self.get_serializer(cart).data, status=status.HTTP_200_OK)
