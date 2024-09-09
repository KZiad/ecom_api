from .models import Product
from rest_framework import viewsets, mixins, filters
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ProductFilter
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="List all products",
    responses={200: ProductSerializer(many=True)}
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary='Retrieve a product',
    responses={200: ProductSerializer()}
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary='Create a product',
    responses={201: ProductSerializer()}
))
class ProductViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.ListModelMixin):
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
