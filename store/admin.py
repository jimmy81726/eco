from django.contrib import admin
from .models import Category, Order, Customer, Product

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product)
