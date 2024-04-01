from django.contrib import admin

from store.models import Products, Order, LigneCommande, Cart, ProductCart, Categories

# Register your models here.

admin.site.register(Products)
admin.site.register(Order)
admin.site.register(LigneCommande)
admin.site.register(Cart)
admin.site.register(ProductCart)
admin.site.register(Categories)
