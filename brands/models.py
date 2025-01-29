from django.db import models
from .base_models import BaseModel


class Brand(BaseModel):
    logo = models.ImageField(upload_to='brands_images/')