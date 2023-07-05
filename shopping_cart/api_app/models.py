from django.db import models
from django.db.models import Model


class CartItem(Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

    objects = models.Manager()