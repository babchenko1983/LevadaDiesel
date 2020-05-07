from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from carts.views import Cart


def order_create(request):
    the_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_id)


    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print('ok')
            order = form.save()
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(order=order,
                                         product=item.product,
                                         number=item.product.number,
                                         quantity=item.quantity,
                                         total_price=cart.total)

            a = OrderItem.objects.all().last().total_price

            try:
                del request.session['cart_id']
            except KeyError:
                pass
            cart.delete()


            return render(request, 'order.html',
                          {'order': order, 'a': a,
                           })
        else:
            form = OrderCreateForm
            return render(request, 'checkout.html',
                          {'cart': cart, 'form': form})




    else:
        print('no')
        form = OrderCreateForm
        return render(request, 'checkout.html',
                      {'cart': cart, 'form': form})
