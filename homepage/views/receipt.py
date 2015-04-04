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
from django.core.mail import send_mail

templater = get_renderer('homepage')

##########################################################################
# shows the list of orders
@view_function
def process_request(request):
    send_mail('Receipt', 'Thank you for ordering from The Colonial Heritage Foundation!', 'from@example.com', ['meservy@gmail.com'], fail_silently=False)
    return templater.render_to_response(request, 'receipt.html')