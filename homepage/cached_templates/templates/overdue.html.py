# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426607227.731911
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!--nothing to import-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        __M_writer('\r\n\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t    <tr>\r\n\t      <th>ID</th>\r\n\t      <th>Due Date</th>\r\n\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t<tr>\r\n            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t<td> ')
            __M_writer(str( overdue[5] ))
            __M_writer(' </td>\r\n\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/overdue.html", "uri": "overdue.html", "source_encoding": "ascii", "line_map": {"66": 60, "35": 1, "40": 18, "46": 5, "59": 14, "53": 5, "54": 11, "55": 12, "56": 13, "57": 13, "58": 14, "27": 0, "60": 17}}
__M_END_METADATA
"""
