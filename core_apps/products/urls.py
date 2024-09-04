from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
]
