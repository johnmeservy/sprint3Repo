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
# shows the list of areas
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    areas = hmod.Area.objects.all().order_by('id')
    params['areas'] = areas

    return templater.render_to_response(request, 'areas.html', params)


###########################################################################
# edits a single area
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        area = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas/')

    # create the form object
    # fill the form initially with data
    form = AreaEditForm(initial={
        'name': area.name,
        'description': area.description,
        'place_number': area.place_number,
    })
    if request.method == 'POST':
        form = AreaEditForm(request.POST)
        form.eventid = area.id
        if form.is_valid():
            # make the changes on the area object
            area.name = form.cleaned_data['name']
            area.description = form.cleaned_data['description']
            area.place_number = form.cleaned_data['place_number']
            area.save()
            return HttpResponseRedirect('/homepage/areas/')

    # store the form in the parameters
    params['form'] = form
    params['area'] = area
    return templater.render_to_response(request, 'areas.edit.html', params)


class AreaEditForm(forms.Form):
    name = forms.CharField(required=True, min_length=1, max_length=100, label="Area Name", widget=forms.TextInput(attrs={'placeholder': 'Area Name', 'class': 'form-control'}))
    description = forms.CharField(required=True, min_length=1, max_length=250, label="Description", widget=forms.TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}))
    place_number = forms.IntegerField(required=True, label="Place Number", widget=forms.TextInput(attrs={'placeholder': 'Place Number', 'class': 'form-control'}))

    def clean_data(self):
        # check if the zip is not 5
        if len(self.cleaned_data['place_number']) < 3:
            raise forms.ValidationError('Invalid number.')

        return self.cleaned_data['place_number']


##########################################################################
# create a new area
@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new area'''
    area = hmod.Area()
    area.name = ''
    area.description = ''
    area.place_number = ''
    # area.event = ''
    area.save()

    return HttpResponseRedirect('/homepage/areas.edit/{}/'.format(area.id))


##########################################################################
# delete a new area
@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')
    '''Delete a area'''
    try:
        area = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas/')

    area.delete()
    return HttpResponseRedirect('/homepage/areas/')
