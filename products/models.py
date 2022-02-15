from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100,)
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,)