# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423215777.840839
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\test_dmp\\homepage\\templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center', 'content_left', 'jumbotron', 'content_right', 'content']


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
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
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
        event = context.get('event', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Edit Event: ')
        __M_writer(str(event.event_name))
        __M_writer('</h2>\r\n\t<form class= "edit_table" method = "POST" >\r\n\r\n')
        __M_writer('\r\n')
        for field in form:
            __M_writer('        <div class="form-group">\r\n            <label for=')
            __M_writer(str(field.name))
            __M_writer('>')
            __M_writer(str(field.label))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('</label>\r\n            ')
            __M_writer(str( field ))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('\t\t\t\t<hr>\r\n\t\t\t\t<button class="btn btn-success" type="submit">Submit</button>\r\n\t\t\t\t<a class="btn btn-default" href="/homepage/events">Cancel</a>\r\n\t\t\t\t<a href = "/homepage/events.delete/')
        __M_writer(str( event.id ))
        __M_writer('/" class="btn btn-danger pull-right">Delete</a>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Taylor\\test_dmp\\homepage\\templates/events.edit.html", "line_map": {"64": 34, "131": 5, "132": 7, "69": 37, "134": 13, "135": 14, "136": 15, "137": 16, "138": 16, "75": 33, "140": 16, "141": 16, "142": 16, "59": 31, "144": 17, "81": 33, "146": 23, "147": 23, "139": 16, "87": 30, "153": 147, "27": 0, "93": 30, "133": 7, "99": 27, "145": 20, "105": 27, "44": 1, "111": 36, "49": 25, "117": 36, "54": 28, "123": 5, "143": 17}, "uri": "events.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
