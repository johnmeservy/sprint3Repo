# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428002170.036121
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'content_center', 'jumbotron', 'content_left', 'content_right']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        amount = context.get('amount', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h2>Enter Checkout Information</h2>\r\n\t<form>\r\n\t\tCredit Card Number<br>\r\n\t\t<input type="text" name="Credit Card">\r\n\t\t<br>\r\n\t\tStreet Address<br>\r\n\t\t<input type="text" name="Address">\r\n\t\t<br>\r\n\t\tCity<br>\r\n\t\t<input type="text" name="City">\r\n\t\t<br>\r\n\t\tState<br>\r\n\t\t<input type="text" name="State">\r\n\t\t<br>\r\n\t\tZIP<br>\r\n\t\t<input type="text" name="Zip">\r\n\t\t<br>\r\n\t</form>\r\n\t<h4>\r\n\t\tTotal Amount: $')
        __M_writer(str( amount ))
        __M_writer('\r\n\t</h4>\r\n\t<a class="btn btn-success" href="/homepage/receipt">Complete Purchase</a>\r\n\t<a class="btn btn-default" href="/homepage/productlist">Cancel</a>\r\n')
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


"""
__M_BEGIN_METADATA
{"line_map": {"80": 3, "130": 38, "100": 29, "136": 130, "73": 3, "106": 29, "43": 1, "112": 32, "48": 27, "81": 23, "82": 23, "53": 30, "118": 32, "88": 35, "58": 33, "27": 0, "124": 38, "94": 35, "63": 36}, "uri": "checkout.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/checkout.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
