from rest_framework import viewsets, status
from .models import Order, Order_Item
from core_apps.carts.models import Cart
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema, no_body


class OrderViewset(viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(operation_summary='Create an order from the user cart',
                         request_body=no_body,
                         responses={201: OrderSerializer(), 400: 'Cart is empty'})
    def create(self, request, *args, **kwargs):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)

        if cart.items.count() == 0:
            return Response({'message': 'Cart is empty'},
                            status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)
        for item in cart.items.all():
            Order_Item.objects.create(
                product_name=item.product.name,
                product_price=item.product.price,
                product_quantity=item.quantity,
                product=item.product,
                order=order
            )
        cart.items.all().delete()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_summary='List all user orders',
                         request_body=no_body,
                         responses={200: OrderSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Order.objects.filter(user=user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
