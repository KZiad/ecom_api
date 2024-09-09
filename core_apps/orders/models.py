# Create your models here
from django.db import models
from core_apps.products.models import Product
from rest_framework.authentication import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return f"Order for {self.user}"

    @property
    def total(self):
        return sum([item.total for item in self.items.select_related('product')])

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Order_Item(models.Model):
    product_name = models.CharField(
        max_length=255)
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField(
        default=1)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.product_name} x {self.product_quantity}"

    @property
    def total(self):
        return self.product_price * self.product_quantity
