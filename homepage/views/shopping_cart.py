from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.models import check_password
from django.contrib.auth import authenticate, login, logout
import random


templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}

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

    return templater.render_to_response(request, 'shoppingcart.form.html', params)


@view_function
def add(request):
    params = {}

    pid = request.urlparams[0]
    qty = request.urlparams[1]

    if pid and qty:
        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session.get('cart', {})

        if pid in cart:
            cart[pid] = int(cart[pid]) + int(qty)
        else:
            cart[pid] = int(qty)

        request.session['cart'] = cart

        p = hmod.Product.objects.get(id=pid)

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
    else:
        return HttpResponseRedirect('/homepage/shoppingcart/')

    return templater.render_to_response(request, 'shoppingcart.html', params)


@view_function
def delete(request):

    params = {}

    pid = request.urlparams[0]

    value_to_remove = pid

    cart = request.session.get('cart', {})
    cart.pop(pid)

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

    return templater.render_to_response(request, 'shoppingcart.form.html', params)
