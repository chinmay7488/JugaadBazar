from django.contrib import admin
from Home.models import Product, CustomUserModel

# Register your models here.
admin.site.register(Product)
admin.site.register(CustomUserModel)