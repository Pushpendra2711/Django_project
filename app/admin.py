from django.contrib import admin
from .models import loc_user,Product_Category,Products
#from django.contrib.auth.models import User

# Register your models here.
admin.site.register(loc_user)
admin.site.register(Product_Category)
admin.site.register(Products)

