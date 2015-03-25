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
        'rental_time': rental.rental_time,
        'due_date': rental.due_date,
        'discount_percent': rental.discount_percent,
        'user': rental.user,
    })
    if request.method == 'POST':
        form = RentalEditForm(request.POST)
        form.rentalid = rental.id
        if form.is_valid():
            # make the changes on the rental object
            rental.rental_time = form.cleaned_data['rental_time']
            rental.due_date = form.cleaned_data['due_date']
            rental.discount_percent = form.cleaned_data['discount_percent']
            rental.user = form.cleaned_data['user']
            rental.save()
            return HttpResponseRedirect('/homepage/rentals/')

    # store the form in the parameters
    params['form'] = form
    params['rental'] = rental
    return templater.render_to_response(request, 'rentals.edit.html', params)


class RentalEditForm(forms.Form):
    rental_time = forms.DateTimeField(required=True, label="Rental Time", widget=forms.TextInput(attrs={'placeholder': 'Rental Time', 'class': 'form-control'}))
    due_date = forms.DateField(required=True, label="Due Date", widget=forms.TextInput(attrs={'placeholder': 'Due Date', 'class': 'form-control'}))
    discount_percent = forms.CharField(required=True, label="Discount Percent", widget=forms.TextInput(attrs={'placeholder': 'Discount Percent', 'class': 'form-control'}))
    user = forms.CharField(required=False, label="User", widget=forms.TextInput(attrs={'placeholder': 'User', 'class': 'form-control'}))

    def clean_data(self):
        # check if the made_to_rental_products is not 5
        if len(self.cleaned_data['discount_percent']) > 2:
            raise forms.ValidationError('Invalid Percent.')

        return self.cleaned_data['discount_percent']


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
    # rental.rental_time = ''
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
