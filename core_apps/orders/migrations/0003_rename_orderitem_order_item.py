# Generated by Django 4.1.7 on 2024-09-04 13:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_remove_product_quantity"),
        ("orders", "0002_alter_order_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderItem",
            new_name="Order_Item",
        ),
    ]
