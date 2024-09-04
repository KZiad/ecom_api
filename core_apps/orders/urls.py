from django.urls import path
from .views import OrderViewset


urlpatterns = [
    path('', OrderViewset.as_view(
        {'get': 'list', 'post': 'create'}), name='order-list'),
]
