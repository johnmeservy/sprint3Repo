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
    delta30 = datetime.timedelta(days=-30)
    delta60 = datetime.timedelta(days=-60)
    delta90 = datetime.timedelta(days=-90)
    overdue = now + delta
    overdue30 = now + delta30
    overdue60 = now + delta60
    overdue90 = now + delta90

    cursor.execute('SELECT * FROM homepage_RentalItem WHERE ((returned = False) AND (due_date between %s and %s))', [overdue30, overdue])
    overdue = cursor.fetchall()

    cursor.execute('SELECT * FROM homepage_RentalItem WHERE ((returned = False) AND (due_date between %s and %s))', [overdue60, overdue30])
    overdue30 = cursor.fetchall()

    cursor.execute('SELECT * FROM homepage_RentalItem WHERE ((returned = False) AND (due_date between %s and %s))', [overdue90, overdue60])
    overdue60 = cursor.fetchall()

    cursor.execute('SELECT * FROM homepage_RentalItem WHERE ((returned = False) AND (due_date < %s))', [overdue90])
    overdue90 = cursor.fetchall()

    params['overdues'] = overdue
    params['overdues30'] = overdue30
    params['overdues60'] = overdue60
    params['overdues90'] = overdue90
    return templater.render_to_response(request, 'overdue.html', params)
