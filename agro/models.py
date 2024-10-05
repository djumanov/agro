from django.db import models
from ckeditor.fields import RichTextField


class FruitType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='fruit_types/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    fruit_type = models.ForeignKey(FruitType, on_delete=models.CASCADE, related_name='fruits')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='fruits/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fruit_type.name}"
