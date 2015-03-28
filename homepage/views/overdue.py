from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
from django.db import connection, connections
import time, datetime

templater = get_renderer('homepage')

##########################################################################
# shows the list of all overdue rentals
@view_function
def process_request(request):
    params = {}
    cursor = connection.cursor()

    now = datetime.date.today()
    delta = datetime.timedelta(days=0)
    overdue = now + delta
    print(now)
    print(delta)
    print(overdue)

    cursor.execute('SELECT * FROM homepage_RentalItem WHERE ((returned = False) AND (due_date < %s))', [overdue])
    overdue = cursor.fetchall()

    params['overdues'] = overdue
    return templater.render_to_response(request, 'overdue.html', params)

