# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427778958.405417
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center', 'content_right', 'content_left', 'content', 'jumbotron']


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
        overdues = context.get('overdues', UNDEFINED)
        overdues60 = context.get('overdues60', UNDEFINED)
        overdues30 = context.get('overdues30', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        overdues90 = context.get('overdues90', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
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
        

        __M_writer('\r\n\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        overdues = context.get('overdues', UNDEFINED)
        overdues60 = context.get('overdues60', UNDEFINED)
        def content():
            return render_content(context)
        overdues30 = context.get('overdues30', UNDEFINED)
        overdues90 = context.get('overdues90', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "text-left">\r\n      <h2>Overdue Items</h2>\r\n    </div>\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"><30 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Item ID</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"> 30-59 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Item ID</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues30:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">60-89 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Item ID</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues60:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">90+ Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Item ID</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues90:
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
{"line_map": {"128": 18, "129": 18, "130": 21, "131": 29, "132": 30, "133": 31, "134": 31, "135": 32, "136": 32, "137": 35, "138": 43, "139": 44, "140": 45, "141": 45, "142": 46, "143": 46, "144": 49, "145": 57, "146": 58, "147": 59, "148": 59, "149": 60, "150": 60, "151": 63, "27": 0, "157": 66, "163": 66, "169": 163, "46": 1, "51": 64, "56": 67, "61": 70, "66": 73, "71": 76, "77": 72, "83": 72, "89": 75, "95": 75, "101": 69, "107": 69, "113": 5, "123": 5, "124": 15, "125": 16, "126": 17, "127": 17}, "source_encoding": "ascii", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html", "uri": "overdue.html"}
__M_END_METADATA
"""
