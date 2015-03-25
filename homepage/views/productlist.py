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
# shows the list of products
@view_function
def process_request(request):

    params = {}

    products = hmod.Product.objects.all()
    params['products'] = products

    return templater.render_to_response(request, 'productlist.html', params)

###########################################################################
# edits a single product
@view_function
def viewproduct(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}
    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/productlist/')

    params['product'] = product
    return templater.render_to_response(request, 'productlist.viewproduct.html', params)


class ProductEditForm(forms.Form):

    category = forms.CharField(required=True, label="Category", widget=forms.TextInput(attrs={'placeholder': 'Category', 'class': 'form-control'}))
    current_price = forms.DecimalField(required=True, label="Current Price", widget=forms.TextInput(attrs={'placeholder': 'Current Price', 'class': 'form-control'}))
    producer_name = forms.CharField(required=False, min_length=1, max_length=15, label="Producer Name", widget=forms.TextInput(attrs={'placeholder': 'Producer Name', 'class': 'form-control'}))

    def clean_data(self):
        # check if the made_to_product_products is not 5
        if len(self.cleaned_data['current_price']) > 10:
            raise forms.ValidationError('Invalid price.')

        return self.cleaned_data['current_price']