from django.db import models


class Product(models.Model):
    """
    Product model
    """
    product_title = models.CharField(max_length=40)
    product_image = models.CharField(max_length=200)
    product_purchase_count = models.PositiveIntegerField(default=0)


class User(models.Model):
    """
    User model
    """
    pass
