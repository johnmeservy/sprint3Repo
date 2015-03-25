# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426607138.314258
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/productlist.viewproduct.html'
_template_uri = 'productlist.viewproduct.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_left', 'content_center', 'content', 'content_right', 'jumbotron']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class = "text-left">\r\n      <h2>Product Detail - ')
        __M_writer(str( product.name ))
        __M_writer('</h2>\r\n    </div>\r\n\r\n    <div align="center">\r\n    \t<img height="100" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/product_images/')
        __M_writer(str( product.photo ))
        __M_writer('" alt="">\r\n    </div>\r\n\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t    <tr>\r\n\t      <th>Description</th>\r\n\t      <th>Category</th>\r\n\t      <th>Current Price</th>\r\n  \t  \t  <th>Producer Name</th>\r\n\t      <th>Actions</th>\r\n\t    </tr>\r\n\t\t  <tr>\r\n          <td> ')
        __M_writer(str( product.description ))
        __M_writer(' </td>\r\n          <td> ')
        __M_writer(str( product.category ))
        __M_writer(' </td>\r\n\t      <td> ')
        __M_writer(str( product.current_price ))
        __M_writer(' </td>\r\n          <td> ')
        __M_writer(str( product.producer_name ))
        __M_writer(' </td>\r\n          <td width="20%" nowrap>\r\n          \t<div class="row">\r\n          \t\t<div class="col-lg-12">\r\n          \t\t\t<div class="input-group">\r\n          \t\t\t\t<input id="quantity_')
        __M_writer(str( product.id))
        __M_writer('" type="text" class="form-control" placeholder="Qty">\r\n          \t\t\t\t<span class="input-group-btn">\r\n          \t\t\t\t\t<button id="product_')
        __M_writer(str(product.id))
        __M_writer('" data-pid="')
        __M_writer(str(product.id))
        __M_writer('" class="btn btn-warning" type="button">Add to Cart</button>\r\n          \t\t\t\t</span>\r\n          \t\t\t</div>\r\n          \t\t</div>\r\n          \t</div>\r\n          </td>\r\n\t\t</tr>\r\n\t</table>\r\n')
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
{"filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/productlist.viewproduct.html", "uri": "productlist.viewproduct.html", "source_encoding": "ascii", "line_map": {"64": 47, "132": 49, "118": 25, "44": 1, "74": 43, "138": 49, "80": 43, "86": 46, "27": 0, "92": 46, "150": 3, "144": 3, "98": 6, "123": 33, "49": 4, "156": 150, "106": 6, "107": 8, "108": 8, "109": 12, "110": 12, "111": 12, "112": 12, "113": 23, "114": 23, "115": 24, "116": 24, "117": 25, "54": 41, "119": 26, "120": 26, "121": 31, "122": 31, "59": 44, "124": 33, "125": 33, "126": 33}}
__M_END_METADATA
"""
