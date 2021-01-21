from django.contrib import admin

from .models.Category import Category
from .models.Product import Product


# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['category']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
