from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: E£{self.price}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
