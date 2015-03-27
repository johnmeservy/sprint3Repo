from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.shortcuts import redirect
import random


templater = get_renderer('homepage')


##########################################################################
# shows the list of events
@view_function
def process_request(request):

    params = {}

    events = hmod.Event.objects.all().order_by('id')
    params['events'] = events

    return templater.render_to_response(request, 'events.html', params)


###########################################################################
# edits a single event
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    # create the form object
    # fill the form initially with data
    form = EventEditForm(initial={
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,
        'map_file_name': event.map_file_name,
        'venue_name': event.venue_name,
        'address1': event.address1,
        'city': event.city,
        'state': event.state,
        'zipcode': event.zipcode
    })
    if request.method == 'POST':
        form = EventEditForm(request.POST)
        form.eventid = event.id
        if form.is_valid():
            # make the changes on the event object
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.map_file_name = form.cleaned_data['map_file_name']
            event.venue_name = form.cleaned_data['venue_name']
            event.address1 = form.cleaned_data['address1']
            event.city = form.cleaned_data['city']
            event.state = form.cleaned_data['state']
            event.zipcode = form.cleaned_data['zipcode']
            event.save()
            return HttpResponseRedirect('/homepage/events/')

    # store the form in the parameters
    params['form'] = form
    params['event'] = event
    return templater.render_to_response(request, 'events.edit.html', params)


class EventEditForm(forms.Form):
    name = forms.CharField(required=True, min_length=1, max_length=100, label="Event Name", widget=forms.TextInput(attrs={'placeholder': 'Event Name', 'class': 'form-control'}))
    description = forms.CharField(required=False, min_length=1, max_length=250, label="Event Description", widget=forms.TextInput(attrs={'placeholder': 'Event Description', 'class': 'form-control'}))
    start_date = forms.DateField(required=True, label="Start Date", widget=forms.TextInput(attrs={'placeholder': 'Start Date', 'class': 'form-control'}))
    end_date = forms.DateField(required=True, label="End Date", widget=forms.TextInput(attrs={'placeholder': 'End Date', 'class': 'form-control'}))
    map_file_name = forms.CharField(required=False, min_length=1, max_length=100, label="Map File Name", widget=forms.TextInput(attrs={'placeholder': 'Map File Name', 'class': 'form-control '}))
    venue_name = forms.CharField(required=False, min_length=1, max_length=100, label="Venue Name", widget=forms.TextInput(attrs={'placeholder': 'Venue Name', 'class': 'form-control '}))
    address1 = forms.CharField(required=True, min_length=1, max_length=100, label="address1", widget=forms.TextInput(attrs={'placeholder': 'address1', 'class': 'form-control'}))
    city = forms.CharField(required=True, min_length=1, max_length=100, label="City", widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(required=True, min_length=1, max_length=100, label="State", widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode = forms.CharField(required=True, label="zipcode Code", widget=forms.TextInput(attrs={'placeholder': 'zipcode Code', 'class': 'form-control'}))

    def clean_data(self):
        # check if the zipcode is not 5
        if len(self.cleaned_data['zipcode']) == 5:
            raise forms.ValidationError('Invalid zipcode Code.')

        return self.cleaned_data['zipcode']


##########################################################################
# create a new event
@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new event'''
    event = hmod.Event()
    event.name = ''
    event.description = ''
    # event.start_date = ''
    # event.end_date = ''
    event.map_file_name = ''
    event.venue_name = ''
    event.address1 = ''
    event.city = ''
    event.state = ''
    # event.zipcode = ''
    event.save()

    return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event.id))


##########################################################################
# delete a new event
@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Delete a event'''
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    event.delete()
    return HttpResponseRedirect('/homepage/events/')
