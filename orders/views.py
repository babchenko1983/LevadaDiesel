from django.shortcuts import render
from .forms import OrderCreateForm
from carts.views import Cart
from send_email.views import index2
from .models import OrderItem


def order_create(request):
    the_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if order.delivery == 'dhl or dpd':
                cart.total+=20
            elif order.delivery == 'europe':
                cart.total+=40
                cart.save()
            index2(request)
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(order=order,
                                         product=item.product,
                                         number=item.product.number,
                                         quantity=item.quantity,
                                         total_price=cart.total)

            a = int(OrderItem.objects.all().last().total_price)
            b = order.payment == 'Visa, Master Card'

            return render(request, 'order.html',
                          {'order': order, 'a': a,
                           "b":b,
                           })
        else:
            form = OrderCreateForm
            return render(request, 'checkout.html',
                          {'cart': cart, 'form': form})




    else:
        form = OrderCreateForm
        return render(request, 'checkout.html',
                      {'cart': cart, 'form': form})


def back(request):
    the_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_id)
    try:
        del request.session['cart_id']
    except KeyError:
        pass
    cart.delete()
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'policy.html')
