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

    return templater.render_to_response(request, 'ajaxtest2.html', params)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass

    params['form'] = form
    return templater.render_to_response(request, 'ajaxtest2.loginform.html', params)
