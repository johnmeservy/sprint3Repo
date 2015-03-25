# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425778680.899734
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/accounts.edit.html'
_template_uri = 'accounts.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'jumbotron', 'content_center', 'content_left', 'content']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h2>Edit User: ')
        __M_writer(str(request.user.get_full_name()))
        __M_writer('</h2>\r\n\t\t<form class="edit_table" method = "POST">\r\n')
        for field in form:
            __M_writer('\t\t\t\t<div class="form-group">\r\n\t\t\t\t\t<label for = ')
            __M_writer(str(field.name))
            __M_writer('> ')
            __M_writer(str(field.label))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer(' </label>\r\n\t\t\t\t\t')
            __M_writer(str( field ))
            __M_writer('\r\n\t\t\t\t</div>\r\n')
        __M_writer('\t\t\t<hr>\r\n\t\t\t\t<button class="btn btn-success" type="submit">Submit</button>\r\n\t\t\t\t<a class="btn btn-warning" href="/homepage/accounts.password/')
        __M_writer(str( user.id ))
        __M_writer('/">Change Password</a>\r\n\t\t\t\t<a class="btn btn-default" href="/homepage/accounts">Cancel</a>\r\n\t\t\t\t<a href="/homepage/accounts.delete/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-danger pull-right">Delete</a>\r\n\t\t\t</hr>\r\n\t\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 29, "139": 9, "132": 4, "133": 5, "134": 5, "135": 7, "136": 8, "137": 9, "138": 9, "75": 31, "140": 9, "141": 9, "142": 9, "143": 10, "144": 10, "81": 31, "146": 15, "147": 15, "148": 17, "149": 17, "87": 22, "27": 0, "93": 22, "99": 28, "145": 13, "105": 28, "45": 1, "111": 25, "50": 20, "155": 149, "117": 25, "55": 23, "123": 4, "60": 26}, "uri": "accounts.edit.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/accounts.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
