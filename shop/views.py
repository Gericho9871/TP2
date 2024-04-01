from django.shortcuts import render
from store.models import Categories


def base_view(request):
    categorie = Categories.objects.all()
    return render(request, 'templates/base.html', {"categories": categorie})
    pass