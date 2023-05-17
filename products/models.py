from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    platform = models.ForeignKey('Platform', null=True, blank=True, on_delete=models.SET_NULL)
    year = models.IntegerField()
    description = models.TextField()
    condition = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
