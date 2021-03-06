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
# shows the list of rentalitems
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    rentalitems = hmod.RentalItem.objects.all().order_by('id')
    params['rentalitems'] = rentalitems

    print('asdfasdfasdfasdf')

    return templater.render_to_response(request, 'rentals.report.html', params)
