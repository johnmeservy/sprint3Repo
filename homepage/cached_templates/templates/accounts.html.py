# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425778568.269095
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/accounts.html'
_template_uri = 'accounts.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content', 'content_center', 'content_left', 'jumbotron']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-left">\r\n\t\t<h2>Manage Account</h2>\r\n\t</div>\r\n\t<table id="manage_table" class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>Username</th>\r\n\t\t\t<th>First Name</th>\r\n\t\t\t<th>Last Name</th>\r\n\t\t\t<th>Email</th>\r\n\t\t\t<th>Actions</th>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> ')
        __M_writer(str( user.username ))
        __M_writer(' </td>\r\n\t\t\t<td> ')
        __M_writer(str( user.first_name ))
        __M_writer(' </td>\r\n\t\t\t<td> ')
        __M_writer(str( user.last_name ))
        __M_writer(' </td>\r\n\t\t\t<td> ')
        __M_writer(str( user.email ))
        __M_writer(' </td>\r\n\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t<a class="label label-info" href="/homepage/accounts.edit/')
        __M_writer(str( user.id ))
        __M_writer('/">Edit Info</a><br>\r\n\t\t\t\t<a class="label label-info" href="/homepage/accounts.password/')
        __M_writer(str( user.id ))
        __M_writer('/">Change Password</a>\r\n\t\t\t</td>\r\n\t\t</tr>\r\n\t</table>\r\n')
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
{"filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/accounts.html", "line_map": {"128": 32, "134": 29, "73": 38, "140": 29, "79": 38, "146": 140, "85": 4, "27": 0, "92": 4, "93": 17, "94": 17, "95": 18, "96": 18, "97": 19, "98": 19, "99": 20, "100": 20, "101": 22, "102": 22, "103": 23, "104": 23, "122": 32, "43": 1, "110": 35, "48": 27, "116": 35, "53": 30, "58": 33, "63": 36}, "source_encoding": "ascii", "uri": "accounts.html"}
__M_END_METADATA
"""
