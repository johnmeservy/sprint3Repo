from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')



##########################################################################
# shows the list of products
@view_function
def process_request(request):

    params = {}

    items = hmod.Item.objects.all()
    params['items'] = items

    return templater.render_to_response(request, 'rentalproductlist.html', params)

# ###########################################################################
# # edits a single product
# @view_function
# def viewproduct(request):
#     if not request.user.is_authenticated():
#         return redirect('/homepage/login/?next=%s' % request.path)
#     if not request.user.is_staff:
#         return HttpResponseRedirect('/homepage/authentication')

#     params = {}
#     try:
#         item = hmod.Item.objects.get(id=request.urlparams[0])
#     except hmod.Item.DoesNotExist:
#         return HttpResponseRedirect('/homepage/rentalproductlist/')

#     params['item'] = item
#     return templater.render_to_response(request, 'rentalproductlist.viewproduct.html', params)
