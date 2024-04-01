import re

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from store.models import Products, Cart ,ProductCart, Order, LigneCommande, Categories

from store.utils import get_cart


def accueil(request):
    products = Products.objects.all()
    categorie = Categories.objects.all()
    return render(request, 'store/index.html', {"products": products, "categorie": categorie})
    pass


def product_by_categorie(request, slug):
    categorie = get_object_or_404(Categories, slug=slug)
    proudct = Products.objects.filter(categorie=categorie)
    categories = Categories.objects.all()
    return render(request, 'store/categorie.html', {"categorie": categorie, "categories": categories, "products": proudct})
    pass


def product_search(request):
    if request.method == "GET" and len(request.GET) > 1:
        product = request.GET["product"]
        try:
            products = Products.objects.filter(nom__icontains=product)
            print(len(products))
            pass
        except:
            raise Http404("Aucun produit correspond à cette recherche n'a été trouvé")
            pass
        return render(request, 'store/index.html')
        pass
    else:
        return render(request, 'store/index.html')
        pass
    pass


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    categories = Categories.objects.all()
    return render(request, 'store/product.html', {"Product": product, "categories": categories})
    pass


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Products, slug=slug)
    cart = None

    if user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=user)
        pass
    else:
        cart = get_cart(request)
        pass

    product_cart, created = ProductCart.objects.get_or_create(product=product, cart=cart)
    if created:
        product.stock -= 1
        product.save()
        messages.success(request, f"{product.nom} a été ajouté à votre panier.")
        pass
    else:
        product_cart.quantity += 1
        product.stock -= 1

        product_cart.save()
        product.save()
        messages.success(request, f"{product.nom} votre panier a été mise à jour.")
        pass

    return redirect('accueil')
    pass


def cart(request):
    cart = None

    try:
        if request.user.is_authenticated:
            cart = request.user.cart
        else:
            cart = get_cart(request)

        if cart:
            products = cart.productcart_set.all()
        else:
            products = []
            pass
        return render(request, 'store/cart.html', {"products": products})
        pass
    except Cart.DoesNotExist:
        messages.warning(request, "Votre panier est vide.")
        return render(request, 'store/cart.html', {"products": []})
        pass
    pass


def delete_cart(request):
    try:
        user = request.user
        if user.is_authenticated:
            if panier := user.cart:
                panier.productcart_set.all().delete()
                panier.delete()
            pass
        else:
            if panier := get_cart(request):
                panier.productcart_set.all().delete()
                panier.delete()
                pass
            pass
        return redirect('accueil')
        pass
    except Cart.DoesNotExist:
        messages.warning(request, "Votre panier est vide.")
        return render(request, 'store/cart.html')
        pass
    pass


def order(request):
    user = request.user
    if user.is_authenticated:
        order, _ = Order.objects.get_or_create(user=user)
        for item in user.cart.productcart_set.all():
            product = item.product
            quantity = item.quantity
            price = item.product.prix_unit
            ligne = LigneCommande(order=order, product=product, quantity=quantity, prix_unit=price)
            ligne.save()
        pass
    return redirect('accueil')
    pass
