# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427578797.366444
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/artisanproductlist.viewproduct.html'
_template_uri = 'artisanproductlist.viewproduct.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content', 'content_left', 'content_center', 'jumbotron']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        artisanproduct = context.get('artisanproduct', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        artisanproduct = context.get('artisanproduct', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class = "text-left">\r\n      <h2>Artisan Product Detail - ')
        __M_writer(str( artisanproduct.name ))
        __M_writer('</h2>\r\n    </div>\r\n\r\n    <div align="center">\r\n    \t<img height="100" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/artisan_product_images/')
        __M_writer(str( artisanproduct.photo ))
        __M_writer('" alt="">\r\n    </div>\r\n\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t    <tr>\r\n\t      <th>Description</th>\r\n\t      <th>Current Price</th>\r\n\t  \t  <th>Artisan Name</th>\r\n\t      <th>Actions</th>\r\n\t    </tr>\r\n\t\t  <tr>\r\n        <td> ')
        __M_writer(str( artisanproduct.description ))
        __M_writer(' </td>\r\n        <td> ')
        __M_writer(str( artisanproduct.low_price ))
        __M_writer(' </td>\r\n        <td> ')
        __M_writer(str( artisanproduct.artisan_name ))
        __M_writer(' </td>\r\n        <td width="20%" nowrap>\r\n        \t<div class="row">\r\n        \t\t<div class="col-lg-12">\r\n        \t\t\t<div class="input-group">\r\n        \t\t\t\t<input id="quantity_')
        __M_writer(str( artisanproduct.id))
        __M_writer('" type="text" class="form-control" placeholder="Qty">\r\n        \t\t\t\t<span class="input-group-btn">\r\n        \t\t\t\t\t<button id="product_')
        __M_writer(str(artisanproduct.id))
        __M_writer('" data-pid="')
        __M_writer(str(artisanproduct.id))
        __M_writer('" class="btn btn-warning" type="button">Add to Cart</button>\r\n        \t\t\t\t</span>\r\n        \t\t\t</div>\r\n        \t\t</div>\r\n        \t</div>\r\n        </td>\r\n\t\t</tr>\r\n\t</table>\r\n')
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
{"uri": "artisanproductlist.viewproduct.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/artisanproductlist.viewproduct.html", "source_encoding": "ascii", "line_map": {"64": 45, "130": 44, "118": 41, "136": 44, "108": 29, "74": 47, "142": 3, "80": 47, "148": 3, "86": 6, "154": 148, "27": 0, "94": 6, "95": 8, "96": 8, "97": 12, "98": 12, "99": 12, "100": 12, "101": 22, "102": 22, "103": 23, "104": 23, "105": 24, "106": 24, "107": 29, "44": 1, "109": 31, "110": 31, "111": 31, "112": 31, "49": 4, "54": 39, "59": 42, "124": 41}}
__M_END_METADATA
"""
