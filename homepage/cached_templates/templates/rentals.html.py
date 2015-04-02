# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428003676.411725
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/rentals.html'
_template_uri = 'rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'content', 'content_center', 'content_right', 'content_left']


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
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<!--create the table-->\r\n    <div class = "text-left">\r\n      <h2>Manage Rentals</h2>\r\n    </div>\r\n    <div class = "text-right">\r\n      <a href ="/homepage/overdue/" class= "btn btn-danger">Overdue Rental Report</a>\r\n      <a href ="/homepage/rentals.create/" class= "btn btn-success">Create New Rental</a>\r\n    </div>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>ID</th>\r\n\t\t      <th>Rental Time</th>\r\n\t\t      <th>Rental Date</th>\r\n\t\t      <th>Actions</th>\r\n\t\t    </tr>\r\n')
        for rental in rentals:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( rental.id ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( rental.time ))
            __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
            __M_writer(str( rental.due_date ))
            __M_writer(' </td>\r\n\t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t\t<a class="label label-info" href="/homepage/rentals.edit/')
            __M_writer(str( rental.id ))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n')
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


"""
__M_BEGIN_METADATA
{"uri": "rentals.html", "source_encoding": "ascii", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/rentals.html", "line_map": {"128": 43, "68": 44, "134": 37, "74": 34, "140": 37, "80": 34, "146": 140, "122": 43, "86": 5, "27": 0, "93": 5, "94": 21, "95": 22, "96": 23, "97": 23, "98": 24, "99": 24, "100": 25, "101": 25, "102": 27, "103": 27, "104": 31, "43": 1, "110": 40, "48": 32, "116": 40, "53": 35, "58": 38, "63": 41}}
__M_END_METADATA
"""
