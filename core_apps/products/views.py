from django.shortcuts import render
from .models import Product
from rest_framework import viewsets, mixins, serializers
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ProductFilter


class ProductViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    ordering = ['price']
    filterset_class = ProductFilter

    def get_permissions(self):

        if self.request.method == 'POST':
            # Only admin can create a product
            permission_classes = [IsAdminUser]
        else:
            # Any user can access products
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
