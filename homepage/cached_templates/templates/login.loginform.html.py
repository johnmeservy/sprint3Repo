# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428183737.700152
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/login.loginform.html'
_template_uri = 'login.loginform.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div id="loginform_container" align="center">\r\n    <form id="loginform" method="POST" action="/homepage/login.loginform/">\r\n      <table>\r\n        ')
        __M_writer(str( form ))
        __M_writer('\r\n      </table>\r\n      <div id="submit_button_container" align="center">\r\n        <button id="submit_button" class="btn btn-warning" type="submit">Login</button>\r\n        <a class="btn btn-link" href="/login.ldap/">Active Directory</button>\r\n        <a class="btn btn-link" href="/password_reset/">Forget Passsword?</button>\r\n      </div>\r\n    </form>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "53": 5, "54": 9, "55": 9, "40": 18, "27": 0, "61": 55, "46": 5}, "uri": "login.loginform.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/login.loginform.html"}
__M_END_METADATA
"""
