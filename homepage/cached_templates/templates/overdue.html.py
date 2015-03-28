# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427504773.164343
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content_left', 'content_center', 'content', 'jumbotron']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        overdues = context.get('overdues', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
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
        

        __M_writer('\r\n\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        overdues = context.get('overdues', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "text-left">\r\n      <h2>Overdue Rentals</h2>\r\n    </div>\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"><30 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">60-90 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">90+ Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
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
{"uri": "overdue.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html", "source_encoding": "ascii", "line_map": {"128": 31, "129": 32, "130": 32, "131": 35, "68": 62, "133": 44, "134": 45, "135": 45, "136": 46, "137": 46, "74": 61, "138": 49, "80": 61, "156": 150, "86": 55, "127": 31, "132": 43, "27": 0, "92": 55, "122": 18, "150": 52, "144": 52, "98": 58, "104": 58, "63": 59, "43": 1, "110": 5, "48": 50, "117": 5, "118": 15, "119": 16, "120": 17, "121": 17, "58": 56, "123": 18, "124": 21, "125": 29, "126": 30, "53": 53}}
__M_END_METADATA
"""
