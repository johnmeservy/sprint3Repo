# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427323621.717161
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/shoppingcart.html'
_template_uri = 'shoppingcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form id="loginform" method="POST" action="/homepage/login.loginform/">\r\n\t\t\t<table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Product Name</th>\r\n          <th>Quantity</th>\r\n          <th>Total</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
        for key in products:
            __M_writer('        ')
            p = products[key] 
            
            __M_writer('\r\n          <tr>\r\n            <td><img class="text-center" height="75" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/product_images/')
            __M_writer(str( p.photo ))
            __M_writer('" alt=""></td>\r\n            <td>')
            __M_writer(str( p.name ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str( cart[str(p.id)] ))
            __M_writer('</td>\r\n            <td>$ ')
            __M_writer(str( p.current_price * cart[str(p.id)] ))
            __M_writer('</td>\r\n            <td width="15%" nowrap>\r\n              <a href="/homepage/shoppingcart.delete/')
            __M_writer(str( p.id ))
            __M_writer('/" data-id="')
            __M_writer(str( p.id ))
            __M_writer('" class="btn btn-danger">Remove</a>\r\n            </td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n  </table>\r\n\r\n  <div id="Total" class="pull-right">\r\n  <h4>Total Amount: $')
        __M_writer(str( amount ))
        __M_writer('</h4>\r\n  </div>\r\n    <div class="btn-group">\r\n      <form method="POST">\r\n        <a class="btn btn-warning" type="Submit" href="/homepage/checkout/">Checkout</a>\r\n      </form>\r\n    </div>\r\n  </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/shoppingcart.html", "uri": "shoppingcart.html", "source_encoding": "ascii", "line_map": {"64": 17, "66": 17, "67": 19, "68": 19, "69": 19, "70": 19, "71": 20, "72": 20, "73": 21, "74": 21, "75": 22, "76": 22, "77": 24, "78": 24, "79": 24, "80": 24, "81": 28, "82": 32, "83": 32, "89": 83, "27": 0, "39": 1, "44": 40, "50": 3, "61": 3, "62": 16, "63": 17}}
__M_END_METADATA
"""
