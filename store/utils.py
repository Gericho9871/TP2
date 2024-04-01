# Dans votre fichier utils.py

from store.models import Cart


def get_cart(request):
    session = request.session
    cart_id = session.get('cart_id')

    if cart_id:
        # Si un identifiant de panier est présent dans la session, essayez de récupérer le panier correspondant
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            # Si le panier n'existe pas, créez-en un nouveau
            cart = Cart.objects.create()
            session['cart_id'] = cart.id
    else:
        # Si l'identifiant de panier n'est pas présent dans la session, créez-en un nouveau
        cart = Cart.objects.create()
        session['cart_id'] = cart.id

    return cart
