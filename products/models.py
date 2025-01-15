from django.db import models
from brands.base_models import BaseModel


class Product(BaseModel):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('catalogs.Category', on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey('colors.Color', on_delete=models.CASCADE, related_name='color')
    image = models.ImageField(upload_to='products_images/')