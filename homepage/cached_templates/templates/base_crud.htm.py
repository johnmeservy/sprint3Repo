# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422524988.086688
_enable_loop = True
_template_filename = 'C:\\Users\\Taylor\\test_dmp\\homepage\\templates/base_crud.htm'
_template_uri = 'base_crud.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>homepage</title>\r\n   \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n    <!-- Latest compiled and minified CSS (BOOTSTRAP) -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\r\n')
        __M_writer('    <link rel="icon" type="image/icon" href="/static/homepage/media/favicon.ico" />\r\n\r\n  \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n  \r\n')
        __M_writer('    <header class="navbar navbar-inverse navbar-fixed-top">\r\n      <div class="container-fluid">\r\n        <!-- Brand and toggle get grouped for better mobile display -->\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="/homepage/index">CHF</a>\r\n        </div>\r\n\r\n        <!-- Collect the nav links, forms, and other content for toggling -->\r\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n          <ul class="nav navbar-nav">\r\n            <li><a href="/homepage/users"><span class ="glyphicon glyphicon-user"></span>  Users</a></li>\r\n          </ul>\r\n\r\n')
        __M_writer('          <ul class="nav navbar-nav navbar-right">\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> Taylor Curtis <span class="caret"></span></a>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="#">Account</a></li>\r\n                <li class="divider"></li>\r\n                <li><a href="#">Log Out</a></li>\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n\r\n        </div><!-- /.navbar-collapse -->\r\n      </div><!-- /.container-fluid -->\r\n    </header>\r\n  \r\n\r\n')
        __M_writer('    <div class="container">\r\n      <div class="row-fluid">\r\n        <div id="content" class="col-xs-12 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n   </div>\r\n\r\n\r\n')
        __M_writer('    <footer class = "navbar navbar-inverse navbar-fixed-bottom">\r\n      <div class="container">\r\n        <p class = "navbar-text pull-left">&copy; 2015 Colonial Heritage Foundation</p>\r\n        <p class = "navbar-text pull-right">Terms of Use | Privacy</p>\r\n      </div>\r\n    </footer>\r\n  \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n              Center Content\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Taylor\\test_dmp\\homepage\\templates/base_crud.htm", "source_encoding": "ascii", "line_map": {"68": 62, "16": 4, "18": 0, "27": 2, "28": 4, "29": 5, "33": 5, "34": 15, "35": 24, "36": 28, "37": 28, "38": 28, "39": 34, "40": 54, "41": 71, "46": 76, "47": 83, "48": 91, "49": 91, "50": 91, "56": 74, "62": 74}, "uri": "base_crud.htm"}
__M_END_METADATA
"""
