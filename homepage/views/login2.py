from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


###########################################################################
# edits a single user
@view_function
def process_request(request):
    params = {}

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/homepage/welcome/')

    # store the form in the parameters
    params['form'] = form

    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, min_length=1, max_length=100, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('Login Failed.  Your username and password were incorrect.')
