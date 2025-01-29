from django.db import models
from brands.base_models import BaseModel


class Product(BaseModel):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('catalogs.Category', on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey('colors.Color', on_delete=models.CASCADE, related_name='color')
    image = models.ImageField(upload_to='products_images/')


    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=200, null=True)
    desc = models.TextField()

    def __str__(self):
        return self.name
