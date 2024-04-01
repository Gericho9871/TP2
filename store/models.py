
from django.db import models
from django.urls import reverse
from django.utils import timezone

from shop.settings import AUTH_USER_MODEL


class Categories(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="categories", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Categorie"
        pass

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})
        pass

    def __str__(self):
        return self.nom
        pass
    pass


class Products(models.Model):
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    prix_unit = models.FloatField()
    stock = models.IntegerField()
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nom} ({self.stock})"
        pass

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})
        pass

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
    pass


class Order(models.Model):
    """
    model pour gérer les commandes
    id_commande
    client
    date
    """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    est_commande = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user}"
        pass
    pass


class LigneCommande(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    prix_unit = models.FloatField()

    class Meta:
        verbose_name = "LigneCommande"
        verbose_name_plural = "LigneCommandes"

    def __str__(self):
        return f"{self.order} {self.product} ({self.quantity})"
        pass
    pass


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(Products, through='ProductCart')

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        pass

    def __str__(self):
        return f"{self.user} {self.product}"
        pass
    pass


class ProductCart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('product', 'cart')
        pass

    def __str__(self):
        return f"{self.cart} {self.product}"
        pass
    pass
