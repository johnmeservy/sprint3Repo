# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428004215.929852
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/rentals.edit.html'
_template_uri = 'rentals.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'content', 'content_left', 'content_center', 'content_right']


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
        rental = context.get('rental', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!--nothing to import-->\r\n\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Edit Rental for: ')
        __M_writer(str( rental.id ))
        __M_writer('</h2>\r\n  <form class= "edit_table" method = "POST" >\r\n\r\n')
        __M_writer('\r\n')
        for field in form:
            __M_writer('        <div class="form-group">\r\n            <label for = ')
            __M_writer(str(field.name))
            __M_writer(' > ')
            __M_writer(str(field.label))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('</label>\r\n            ')
            __M_writer(str( field ))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('\r\n        <hr>\r\n        <button class="btn btn-success" type="submit">Submit</button>\r\n        <a href="/homepage/rentals.delete/')
        __M_writer(str( rental.id ))
        __M_writer('/" class="btn btn-warning">Return</button>\r\n        <a class="btn btn-default" href="/homepage/rentals">Cancel</a>\r\n        <a href = "/homepage/rentals.delete/')
        __M_writer(str( rental.id ))
        __M_writer('/" class="btn btn-danger pull-right">Delete</a>\r\n  </form>\r\n')
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
{"line_map": {"64": 36, "131": 35, "69": 39, "113": 25, "108": 17, "75": 29, "143": 38, "81": 29, "149": 38, "87": 5, "137": 35, "27": 0, "95": 5, "96": 7, "97": 7, "98": 13, "99": 14, "100": 15, "101": 16, "102": 16, "103": 16, "104": 16, "105": 16, "106": 16, "107": 17, "44": 1, "109": 20, "110": 23, "111": 23, "112": 25, "49": 27, "155": 149, "54": 30, "119": 32, "59": 33, "125": 32}, "source_encoding": "ascii", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/rentals.edit.html", "uri": "rentals.edit.html"}
__M_END_METADATA
"""
