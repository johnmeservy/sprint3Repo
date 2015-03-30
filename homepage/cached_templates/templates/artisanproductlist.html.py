# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427579442.949266
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/artisanproductlist.html'
_template_uri = 'artisanproductlist.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center', 'content_right', 'jumbotron', 'content', 'content_left']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        artisanproducts = context.get('artisanproducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form class="navbar-form navbar-left" role="search">\r\n        <div class="input-group">\r\n            <input type="text" class="form-control searchbar" placeholder="Search" name="srch-term" id="srch-term">\r\n            <div class="input-group-btn">\r\n                <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>\r\n            </div>\r\n        </div>\r\n      </form>\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        artisanproducts = context.get('artisanproducts', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        for artisanproduct in artisanproducts:
            __M_writer('\t\t<div class="item_container">\r\n\t\t\t\t<div id="product" class="">')
            __M_writer(str( artisanproduct ))
            __M_writer('</div>\r\n\t\t\t\t<img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/artisan_product_images/')
            __M_writer(str( artisanproduct.photo ))
            __M_writer('"/>\r\n\t\t\t\t<div>Created By: ')
            __M_writer(str( artisanproduct.artisan_name ))
            __M_writer('</div>\r\n\t\t\t\t<div>Sold At: ')
            __M_writer(str( artisanproduct.area ))
            __M_writer('</div>\r\n\t\t\t\t<div id="current_price" class="">$')
            __M_writer(str(artisanproduct.low_price))
            __M_writer('</div>\r\n\t\t\t<div class="text-right">\r\n\t\t\t\t<div class="row">\r\n\t              <div class="col-lg-12">\r\n\t                <div class="input-group">\r\n\t                  \r\n\t                </div>\r\n\t              </div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
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
{"uri": "artisanproductlist.html", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/artisanproductlist.html", "line_map": {"64": 39, "128": 8, "130": 9, "131": 10, "132": 10, "118": 3, "129": 9, "74": 38, "138": 35, "80": 38, "86": 41, "27": 0, "92": 41, "150": 144, "144": 35, "98": 24, "59": 36, "104": 24, "44": 1, "110": 3, "49": 22, "54": 33, "119": 4, "120": 5, "121": 6, "122": 6, "123": 7, "124": 7, "125": 7, "126": 7, "127": 8}, "source_encoding": "ascii"}
__M_END_METADATA
"""
