from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Cart, CartItem
from web.models import Product


def view(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        print("ok")
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            cart.line_total = line_total
            new_total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {'cart': cart}
    else:
        empty_message = "Ваша корзина пуста"
        context = {"empty": True,
                   'empty_message': empty_message, }
    return render(request, 'view.html', context)


def add_to_cart(request, slug):
    request.session.set_expiry(20000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    product = None
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    try:
        qty = request.GET.get('qty')
        update_qty = True

    except:
        qty = 0
        update_qty = False

    if int(qty) <= product.stock:
        product.stock -= int(qty)
        product.save()

        cart_item = CartItem.objects.create(cart=cart, product=product)
        if update_qty and qty:
            if int(qty) == 0:
                cart_item.delete()
            else:
                cart_item.quantity = qty

                cart_item.save()

        else:
            pass

        return HttpResponseRedirect(reverse("cart"))
    else:

        return HttpResponseRedirect(reverse("cart"))


def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))
    cartitem = CartItem.objects.get(id=id)

    cartitem.product.stock += cartitem.quantity
    cartitem.product.save()

    cartitem.cart = None
    cartitem.save()
    cartitem.delete()
    return HttpResponseRedirect(reverse("cart"))
