from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)

    pid = request.urlparams[0]

    cart = request.session.get('cart', {})

    request.session['cart'] = cart

    cart = request.session.get('cart', {})
    products = {}
    amount = 0

    for product in hmod.Product.objects.filter(id__in=cart.keys()):
        products[str(product.id)] = product

    for key in products:
        p = products[key]
        amount += p.current_price * cart[str(p.id)]

    params = {
        'cart': cart,
        'products': products,
        'amount': amount,
    }

    return templater.render_to_response(request, 'checkout.html', params)

