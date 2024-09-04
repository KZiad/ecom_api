from django.db import models
from core_apps.products.models import Product
from rest_framework.authentication import get_user_model
User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cart')

    @property
    def total(self):
        return sum([item.total for item in self.items.select_related('product')])

    def __str__(self):
        return f"Cart for {self.user}"


class Cart_Item(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
