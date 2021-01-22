from django.db import models

from .Category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='product/uploads/')

    @staticmethod
    def getAllProducts():
        return Product.objects.all()

    def getSpecificProducts(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            Product.getAllProducts()
