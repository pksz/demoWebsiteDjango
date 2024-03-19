from django.contrib import admin
from . models import Products
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name",'product_image','product_description')




