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
# shows the list of rentals
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    rentals = hmod.Rental.objects.all().order_by('id')
    params['rentals'] = rentals

    return templater.render_to_response(request, 'rentals.html', params)


###########################################################################
# edits a single rental
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        rental = hmod.Rental.objects.get(id=request.urlparams[0])
    except hmod.Rental.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    # create the form object
    # fill the form initially with data
    form = RentalEditForm(initial={
        'time': rental.time,
        'due_date': rental.due_date,
    })
    if request.method == 'POST':
        form = RentalEditForm(request.POST)
        form.rentalid = rental.id
        if form.is_valid():
            # make the changes on the rental object
            rental.time = form.cleaned_data['time']
            rental.due_date = form.cleaned_data['due_date']
            rental.user = form.cleaned_data['user']
            rental.amount_due = form.cleaned_data['amount_due']
            rental.save()
            return HttpResponseRedirect('/homepage/rentals/')

    # store the form in the parameters
    params['form'] = form
    params['rental'] = rental
    return templater.render_to_response(request, 'rentals.edit.html', params)


class RentalEditForm(forms.Form):
    time = forms.DateTimeField(required=True, label="Rental Time", widget=forms.TextInput(attrs={'placeholder': 'Rental Time', 'class': 'form-control'}))
    due_date = forms.DateField(required=True, label="Due Date", widget=forms.TextInput(attrs={'placeholder': 'Due Date', 'class': 'form-control'}))
    user = forms.CharField(required=False, label="User", widget=forms.TextInput(attrs={'placeholder': 'User', 'class': 'form-control'}))
    amount_due = forms.CharField(required=False, label="Amount Due", widget=forms.TextInput(attrs={'placeholder': 'Amount Due', 'class': 'form-control'}))


##########################################################################
# create a new rental
@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new rental'''
    rental = hmod.Rental()
    user = hmod.User()
    # rental.time = ''
    # rental.due_date = ''
    rental.disocunt_percent = ''
    rental.save()

    return HttpResponseRedirect('/homepage/rentals.edit/{}/'.format(rental.id))


##########################################################################
# delete a new rental
@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Delete a rental'''
    try:
        rental = hmod.Rental.objects.get(id=request.urlparams[0])
    except hmod.Rental.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    rental.delete()
    return HttpResponseRedirect('/homepage/rentals/')