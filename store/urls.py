from django.urls import path

from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('product/<str:slug>/', product_detail, name="product"),
    path('category/<str:slug>/', product_by_categorie, name="category"),

    path('product/<str:slug>/add-to-cart', add_to_cart, name="add-to-cart"),
    path('product/cart', cart, name="cart"),
    path('product/delete', delete_cart, name="delete_cart"),
    path('product/customer/order', order, name="order"),
    path('product/search', product_search, name="product_search"),
]
