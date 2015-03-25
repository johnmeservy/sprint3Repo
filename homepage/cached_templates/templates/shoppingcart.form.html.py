# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427322518.300975
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/shoppingcart.form.html'
_template_uri = 'shoppingcart.form.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'content_right', 'content_center', 'content_left', 'jumbotron']


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
        cart = context.get('cart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        amount = context.get('amount', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart = context.get('cart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        amount = context.get('amount', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form id= "loginform" method ="POST" action="/homepage/login.loginform/">\r\n  <h2>Shopping Cart</h2>\r\n    <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Product Name</th>\r\n          <th>Quantity</th>\r\n          <th>Total</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
        for key in products:
            __M_writer('        ')
            p = products[key] 
            
            __M_writer('\r\n          <tr>\r\n            <td><img class="text-center" height="75" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
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


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 49, "67": 50, "134": 49, "140": 46, "77": 3, "164": 158, "152": 43, "146": 46, "88": 3, "89": 17, "90": 18, "27": 0, "93": 18, "94": 20, "95": 20, "96": 20, "97": 20, "98": 21, "99": 21, "100": 22, "101": 22, "102": 23, "103": 23, "104": 25, "105": 25, "106": 25, "107": 25, "108": 29, "109": 33, "110": 33, "47": 1, "91": 18, "52": 41, "158": 43, "57": 44, "122": 52, "62": 47, "116": 52}, "uri": "shoppingcart.form.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/shoppingcart.form.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
