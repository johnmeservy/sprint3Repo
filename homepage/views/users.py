from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth import authenticate, login, logout



templater = get_renderer('homepage')


##########################################################################
# shows the list of users
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    # grab all users from the table
    # users = hmod.User.objects.all().orderby()
    users = hmod.User.objects.all().order_by('id')

    # print users to console
    print(users)

    # store the users in the parameters to pass to the html
    params['users'] = users

    return templater.render_to_response(request, 'users.html', params)


###########################################################################
# edits a single user
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    # create the form object
    # fill the form initially with data
    form = UserEditForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'password': user.password
    })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            # make the changes on the user object
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()
            return HttpResponseRedirect('/homepage/users/')

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'users.edit.html', params)


class UserEditForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, min_length=1, max_length=100, label="First Name", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, min_length=1, max_length=100, label="Last Name", widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    password = forms.CharField(required=False, min_length=1, max_length=100, label="Password", widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    email = forms.EmailField(required=True, min_length=1, max_length=100, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    # is_staff = forms.BooleanField(required=True, label="Is Staff?", widget=forms.CheckboxInput)

    def clean_username(self):
        # check if the username is more than 6
        if len(self.cleaned_data['username']) < 3:
            raise forms.ValidationError('Please enter a username that is at least 3 characters.')

        # check to see the username already exists
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken")

        return self.cleaned_data['username']


##########################################################################
# create a new user
@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new user'''
    user = hmod.User()
    user.username = str(random.randint(100000, 999999))
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.password = ''
    user.is_superuser = False
    user.is_staff = False
    user.save()

    return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user.id))


##########################################################################
# delete a new user
@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Delete a user'''
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    user.delete()
    return HttpResponseRedirect('/homepage/users/')

# create a new user
@view_function
def newaccount(request):
    '''Creates a new user'''
    user = hmod.User()
    user.is_staff = 'False'
    user.is_active = 'True'
    user.is_superuser = 'False'
    user.username = str(random.randint(100000, 999999))
    user.password = ''
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.address1 = ''
    user.address2 = ''
    user.city = ''
    user.state = ''
    user.zipcode = ''
    user.phone_number = ''
    user.save()

    return HttpResponseRedirect('/homepage/users.new/{}/'.format(user.id))
    
###########################################################################
# edits a single account
@view_function
def new(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/accounts/')

    # create the form object
    # fill the form initially with data
    form = UserNewForm(initial={
        'username': user.username,
        'password': user.password,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address1': user.address1,
        'address2': user.address2,
        'city': user.city,
        'state': user.state,
        'zipcode': user.zipcode,
        'phone_number': user.phone_number,
    })
    if request.method == 'POST':
        form = UserNewForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            # make the changes on the user object
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.address1 = form.cleaned_data['address1']
            user.address2 = form.cleaned_data['address2']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']
            user.zipcode = form.cleaned_data['zipcode']
            user.phone_number = form.cleaned_data['phone_number']
            user.set_password(form.cleaned_data['password'])
            user.save()
            print('user saved')
            username = user.username
            user = authenticate(username=username, password=request.POST['password'])
            login(request, user)
            print('login user.')
            return HttpResponseRedirect('/homepage/accounts/')

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'users.new.html', params)


class UserNewForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, min_length=1, max_length=100, label="Password", widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, min_length=1, max_length=100, label="First Name", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, min_length=1, max_length=100, label="Last Name", widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(required=True, min_length=1, max_length=100, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    address1 = forms.CharField(required=True, min_length=1, max_length=100, label="Address", widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    address2 = forms.CharField(required=False, min_length=1, max_length=100, label="Address 2", widget=forms.TextInput(attrs={'placeholder': 'Address 2', 'class': 'form-control'}))
    city = forms.CharField(required=True, min_length=1, max_length=100, label="City", widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(required=True, min_length=1, max_length=100, label="State", widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode = forms.CharField(required=True, min_length=1, max_length=100, label="Zip", widget=forms.TextInput(attrs={'placeholder': 'Zip', 'class': 'form-control'}))
    phone_number = forms.CharField(required=True, min_length=1, max_length=100, label="Phone", widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    # is_staff = forms.BooleanField(required=True, label="Is Staff?", widget=forms.CheckboxInput)

    def clean_username(self):
        # check if the username is more than 6
        if len(self.cleaned_data['username']) < 3:
            raise forms.ValidationError('Please enter a username that is at least 3 characters.')

        # check to see the username already exists
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken")

        return self.cleaned_data['username']