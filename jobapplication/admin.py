from django.contrib import admin
from .models import *

admin.site.register([
    Customer, Category, Cart,
    CartProduct, Order, Product
])