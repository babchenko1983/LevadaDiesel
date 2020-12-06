from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from orders.models import Order
from carts.models import Cart


def index2(request):
    the_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_id)
    content = cart.cartitem_set.all()
    if request.method == 'POST':
        i = Order.objects.only('email').first()
        to = i.email
        html_content = render_to_string("index2.html", {'content': content,
                                                        'cart': cart,

                                                        })
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'Potwierdzenie',
            text_content,
            'babchenko1983@gmail.com',
            [to],

        )
        email.attach_alternative(html_content, 'text/html')
        email.send()


    else:
        print('yes')

    return render(request, 'index2.html')
