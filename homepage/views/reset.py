from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
from django.db import connection, connections
import time

templater = get_renderer('homepage')

##########################################################################
# shows the list of orders
@view_function
def reset(request):
    password_reset(request[, is_admin_site, homepage/accounts.password.html, homepage/accounts.password.reset.html, password_reset_form, token_generator, post_reset_redirect, from_email, current_app, extra_context, html_email_template_name])
    return templater.render_to_response(request, 'overdue.html', params)