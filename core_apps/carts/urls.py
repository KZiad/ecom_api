from django.urls import path
from .views import CartViewSet

urlpatterns = [
    path('', CartViewSet.as_view({"get": "list"}), name='list_items'),
    path('<int:pk>',
         CartViewSet.as_view({"post": "create", "delete": "destroy"}),
         name='add_remove_item'),
]
