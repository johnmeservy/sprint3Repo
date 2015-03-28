# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427507465.835759
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'content_left', 'jumbotron', 'content_center', 'content_right']


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
        overdues1 = context.get('overdues1', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        overdues3 = context.get('overdues3', UNDEFINED)
        overdues2 = context.get('overdues2', UNDEFINED)
        overdues4 = context.get('overdues4', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        overdues1 = context.get('overdues1', UNDEFINED)
        overdues3 = context.get('overdues3', UNDEFINED)
        overdues2 = context.get('overdues2', UNDEFINED)
        overdues4 = context.get('overdues4', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "text-left">\r\n      <h2>Overdue Rentals</h2>\r\n    </div>\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"><30 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue1 in overdues1:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue1[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue1[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"> 30-59 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue2 in overdues2:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue2[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue2[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">60-89 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue3 in overdues3:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue3[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue3[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">90+ Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue4 in overdues4:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue4[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue4[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
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
{"uri": "overdue.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html", "source_encoding": "ascii", "line_map": {"133": 66, "139": 66, "145": 72, "151": 72, "27": 0, "157": 75, "163": 75, "169": 163, "46": 1, "51": 64, "56": 67, "61": 70, "66": 73, "71": 76, "77": 5, "87": 5, "88": 15, "89": 16, "90": 17, "91": 17, "92": 18, "93": 18, "94": 21, "95": 29, "96": 30, "97": 31, "98": 31, "99": 32, "100": 32, "101": 35, "102": 43, "103": 44, "104": 45, "105": 45, "106": 46, "107": 46, "108": 49, "109": 57, "110": 58, "111": 59, "112": 59, "113": 60, "114": 60, "115": 63, "121": 69, "127": 69}}
__M_END_METADATA
"""
