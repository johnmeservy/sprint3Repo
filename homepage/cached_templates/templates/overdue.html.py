# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427509718.200657
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_left', 'content_right', 'content', 'content_center', 'jumbotron']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        overdues = context.get('overdues', UNDEFINED)
        overdues60 = context.get('overdues60', UNDEFINED)
        overdues30 = context.get('overdues30', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        overdues90 = context.get('overdues90', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        overdues60 = context.get('overdues60', UNDEFINED)
        overdues = context.get('overdues', UNDEFINED)
        def content():
            return render_content(context)
        overdues90 = context.get('overdues90', UNDEFINED)
        overdues30 = context.get('overdues30', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "text-left">\r\n      <h2>Overdue Rentals</h2>\r\n    </div>\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"><30 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center"> 30-59 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues30:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">60-89 Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues60:
            __M_writer('\t\t\t<tr>\r\n\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\t<table id="overdue_table" class = "table table-striped table-bordered">\r\n\t\t<th scope="col" colspan="2"><div align="center">90+ Days </div></th>\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t    </tr>\r\n')
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


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html", "uri": "overdue.html", "line_map": {"128": 45, "129": 45, "130": 46, "131": 46, "132": 49, "133": 57, "134": 58, "135": 59, "136": 59, "137": 60, "138": 60, "139": 63, "145": 72, "151": 72, "27": 0, "157": 66, "163": 66, "169": 163, "46": 1, "51": 64, "56": 67, "61": 70, "66": 73, "71": 76, "77": 69, "83": 69, "89": 75, "95": 75, "101": 5, "111": 5, "112": 15, "113": 16, "114": 17, "115": 17, "116": 18, "117": 18, "118": 21, "119": 29, "120": 30, "121": 31, "122": 31, "123": 32, "124": 32, "125": 35, "126": 43, "127": 44}, "source_encoding": "ascii"}
__M_END_METADATA
"""
