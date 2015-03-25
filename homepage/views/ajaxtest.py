from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')


###########################################################################
# edits a single user
@view_function
def process_request(request):
    params = {}
    return templater.render_to_response(request, 'ajaxtest.html', params)


@view_function
def check_username(request):
    username = request.REQUEST.get['u']
    print('>>>>>>>>>>>>>>>>>>>', username)

    # check that username exists, and does it exist with a different username than the current user
    # if its good
    return HttpResponse("1")
    # if its bad
    return HttpResponse("0")
