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
# shows the list of orders
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    orders = hmod.Order.objects.all().order_by('id')
    params['orders'] = orders

    return templater.render_to_response(request, 'orders.html', params)


###########################################################################
# edits a single order
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        order = hmod.Order.objects.get(id=request.urlparams[0])
    except hmod.Order.DoesNotExist:
        return HttpResponseRedirect('/homepage/orders/')

    # create the form object
    # fill the form initially with data
    form = OrderEditForm(initial={
        'order_date': order.order_date,
        'order_phone': order.order_phone,
        'phone_ext': order.phone_ext,
        'date_packed': order.date_packed,
        'date_paid': order.date_paid,
        'date_shipped': order.date_shipped,
        'tracking_number': order.tracking_number,
    })
    if request.method == 'POST':
        form = OrderEditForm(request.POST)
        form.orderid = order.id
        if form.is_valid():
            # make the changes on the order object
            order.order_date = form.cleaned_data['order_date']
            order.order_phone = form.cleaned_data['order_phone']
            order.phone_ext = form.cleaned_data['phone_ext']
            order.date_packed = form.cleaned_data['date_packed']
            order.date_paid = form.cleaned_data['date_paid']
            order.date_shipped = form.cleaned_data['date_shipped']
            order.tracking_number = form.cleaned_data['tracking_number']
            order.save()
            return HttpResponseRedirect('/homepage/orders/')

    # store the form in the parameters
    params['form'] = form
    params['order'] = order
    return templater.render_to_response(request, 'orders.edit.html', params)


class OrderEditForm(forms.Form):
    order_date = forms.DateField(required=True, label="Order Date", widget=forms.TextInput(attrs={'placeholder': 'Order Date', 'class': 'form-control'}))
    order_phone = forms.CharField(required=True, min_length=1, max_length=15, label="Phone", widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    phone_ext = forms.CharField(required=False, min_length=1, max_length=15, label="Phone Ext.", widget=forms.TextInput(attrs={'placeholder': 'Phone Ext.', 'class': 'form-control'}))
    date_packed = forms.DateField(required=False, label="Date Packed", widget=forms.TextInput(attrs={'placeholder': 'Date Packed', 'class': 'form-control'}))
    date_paid = forms.DateField(required=False, label="Date Paid", widget=forms.TextInput(attrs={'placeholder': 'Date Paid', 'class': 'form-control '}))
    date_shipped = forms.DateField(required=False, label="Date Shipped", widget=forms.TextInput(attrs={'placeholder': 'Date Shipped', 'class': 'form-control '}))
    tracking_number = forms.CharField(required=False, min_length=1, max_length=100, label="Tracking Number", widget=forms.TextInput(attrs={'placeholder': 'Tracking Number', 'class': 'form-control'}))

    def clean_data(self):
        # check if the made_to_order_products is not 5
        if len(self.cleaned_data['phone_ext']) > 5:
            raise forms.ValidationError('Invalid phone ext.')

        return self.cleaned_data['phone_ext']


##########################################################################
# create a new order
@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new order'''
    order = hmod.Order()
    # order.order_date = ''
    order.order_phone = ''
    order.phone_ext = ''
    # order.date_packed = ''
    # order.date_paid = ''
    # order.date_shipped = ''
    order.tracking_number = ''
    # order.customer = ''
    order.save()

    return HttpResponseRedirect('/homepage/orders.edit/{}/'.format(order.id))


##########################################################################
# delete a new order
@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Delete a order'''
    try:
        order = hmod.Order.objects.get(id=request.urlparams[0])
    except hmod.Order.DoesNotExist:
        return HttpResponseRedirect('/homepage/orders/')

    order.delete()
    return HttpResponseRedirect('/homepage/orders/')
