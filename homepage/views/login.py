from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
from django.contrib.auth.models import User

templater = get_renderer('homepage')


###########################################################################
# edits a single user
@view_function
def process_request(request):
    params = {}

    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(label=("Username"), widget=forms.TextInput())
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput())

    def clean(self):
        if len(self.errors) == 0:
            try:
        #   user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                username=self.cleaned_data['username'] + '@cheritage.local'
                password=self.cleaned_data['password']
                s = Server('www.cheritage.org', port = 8889, get_info = GET_ALL_INFO)
                c = Connection(s, username, password, auto_bind = True, client_strategy = STRATEGY_SYNC,  authentication=AUTH_SIMPLE, raise_exceptions=False)
                print(s.info) # display info from the DSE. OID are decoded when recognized by the library
                print(">>>>> print connection results")
                print(c.result)
                print(c.response)
                # return HttpResponse('<script> window.location.href = "/homepage/accounts" </script>')
            except:
                raise forms.ValidationError('Invalid Username or Password.')
            # user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
            # if user is None:
            #     raise forms.ValidationError('Invalid Username or Password.')


@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
        #     try:
            user = authenticate(username='super', password='asdfasdf')
            # if user is None:
                # user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['username']+'@cheritage.org',form.cleaned_data['password'])
            # user = User.objects.get(username='super')
            # user.set_username(form.cleaned_data['username'])
        #         username=form.cleaned_data['username'] + '@cheritage.local'
        #         password=form.cleaned_data['password']
        #         s = Server('www.cheritage.org', port = 8889, get_info = GET_ALL_INFO)
        #         c = Connection(s, username, password, auto_bind = True, client_strategy = STRATEGY_SYNC,  authentication=AUTH_SIMPLE, raise_exceptions=False)
        #         print(s.info) # display info from the DSE. OID are decoded when recognized by the library
        #         print(">>>>> print connection results")
        #         print(c.result)
        #         print(c.response)
            login(request, user)
            return HttpResponse('<script> window.location.href = "/homepage/accounts" </script>')
        #     except:
        #         raise forms.ValidationError('Invalid Username or Password.')


    params['form'] = form
    return templater.render_to_response(request, 'login.loginform.html', params)


@view_function
def check_username(request):
    username = request.REQUEST.get['u']
    password = request.REQUEST.get['p']
    print('>>>>>>>>>>>>', username)

    user = hmod.User.objects.get(username=username)

    return HttpResponse("1")
    return HttpResponse("0")


@view_function
def ldap(request, user):

    user=hmod
    s = Server('www.cheritage.org', port = 8889, get_info = GET_ALL_INFO)
    c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC, user='john@cheritage.local', password='Talkerey60!', authentication=AUTH_SIMPLE, raise_exceptions=False)
    print(s.info) # display info from the DSE. OID are decoded when recognized by the library
    print(">>>>> print connection results")
    print(c.result)
    print(c.response) #it's okay if this is None

#     s = Server('www.cheritage.org', port=8889, get_info=GET_ALL_INFO)
# c = Connection(
#       s,
#       auto_bind = True,
#       user = 'dc\John',
#       password= 'Talkerey5260!',
#       authentication=AUTH_SIMPLE,
#       client_strategy=STRATEGY_SYNC
#     )

# search_results = c.search(
#   search_base = 'CN=Users,DC=dc,DC=chfound,DC=com',
#   search_filter = '(objectClass=person)',
#   attributes = [
#     'givenName',
#     'sn',
#     'mail',]
#   )

# print(c.response_to_json(search_results))