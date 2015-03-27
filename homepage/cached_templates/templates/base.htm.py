# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427489008.343456
_enable_loop = True
_template_filename = 'C:\\Users\\John\\test_dmp\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content_left', 'jumbotron', 'content', 'content_center']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>homepage</title>\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n    <!-- Latest compiled and minified CSS (BOOTSTRAP) -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\r\n    <!-- add a jquery form plug in for ajax calls - http://malsup.com/jquery/form/#download -->\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n\r\n    <!-- add a jquery form plug in for modals - https://github.com/doconix/jquery.loadmodal.js/blob/master/jquery.loadmodal.js -->\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n\r\n    <!--Favicon -->\r\n    <link rel="icon" type="image/icon" href="/static/homepage/media/favicon.ico" />\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n')
        __M_writer('    <header class="navbar navbar-inverse navbar-fixed-top">\r\n      <div class="container-fluid">\r\n        <!-- Brand and toggle get grouped for better mobile display -->\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="/homepage/index">CHF</a>\r\n        </div>\r\n\r\n        <!-- Collect the nav links, forms, and other content for toggling -->\r\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n          <ul class="nav navbar-nav">\r\n            <li><a href="/homepage/users"><span class ="glyphicon glyphicon-user"></span>  Users</a></li>\r\n            <li><a href="/homepage/events"><span class ="glyphicon glyphicon-calendar"></span>  Events</a></li>\r\n            <li><a href="/homepage/areas"><span class ="glyphicon glyphicon-globe"></span>  Areas</a></li>\r\n            <li><a href="/homepage/orders"><span class ="glyphicon glyphicon-file"></span>  Orders</a></li>\r\n            <li><a href="/homepage/products"><span class ="glyphicon glyphicon-list"></span>  Products</a></li>\r\n            <li><a href="/homepage/rentals"><span class ="glyphicon glyphicon-transfer"></span>  Rentals</a></li>\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class ="glyphicon glyphicon-usd"></span>  Shop <span class ="caret"></a>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="/homepage/productlist/">Mass Produced Products</a></li>\r\n                <li><a href="/homepage/artisanproductlist/">Artisan Products</a></li>\r\n                <li><a href="/homepage/rentalproductlist/">Rentable Products</a></li>\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n\r\n')
        if request.user.is_authenticated():
            __M_writer('            <ul class="nav navbar-nav navbar-right">\r\n            <li><a href="/homepage/shoppingcart"><span class ="glyphicon glyphicon-shopping-cart"></span></a></li>\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> ')
            __M_writer(str(request.user.get_full_name() ))
            __M_writer(' <span class="caret"></span></a>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="/homepage/accounts/">My Account</a></li>\r\n                <li class="divider"></li>\r\n                <li><a href="/homepage/logout">Log Out</a></li>\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n')
        else:
            __M_writer('            <ul class="nav navbar-nav navbar-right">\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> My Account <span class="caret"></span></a>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="/homepage/users.newaccount/" class="btn btn-block btn-link">Create Account</a></li>\r\n                <li class="divider"></li>\r\n                <li><button id="show_login_dialog" class="btn btn-block btn-link">Login</button></li>\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n')
        __M_writer('\r\n\r\n        </div><!-- /.navbar-collapse -->\r\n      </div><!-- /.container-fluid -->\r\n    </header>\r\n\r\n')
        __M_writer('    <div class = "jumbotron">\r\n      <div class = "container-fluid">\r\n        <div class="row">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n')
        __M_writer('    <div class="container">\r\n      <div class="row-fluid">\r\n        <div class="col-xs-12 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n')
        __M_writer('    <div class="container">\r\n      <div class="row-fluid">\r\n        <div class="col-xs-4 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <div class="col-xs-4 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <div class="col-xs-4 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n')
        __M_writer('    <footer class = "navbar navbar-inverse navbar-fixed-bottom">\r\n      <div class="container">\r\n        <p class = "navbar-text pull-left">&copy; 2015 Colonial Heritage Foundation</p>\r\n        <p class = "navbar-text pull-right">Terms of Use | Privacy</p>\r\n      </div>\r\n    </footer>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n              Right Content\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n              Left Content\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\r\n              <h1>WELCOME!</h1>\r\n              <p>This is where the description goes.</p>\r\n              <a class = "btn btn-success">Success!</a>\r\n              <a class = "btn btn-primary">Primary</a>\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n              Left Content\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n              Center Content\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"132": 120, "138": 120, "16": 4, "18": 0, "150": 136, "156": 150, "36": 2, "37": 4, "38": 5, "42": 5, "43": 15, "44": 24, "45": 24, "46": 27, "47": 27, "48": 34, "49": 34, "50": 34, "51": 40, "52": 72, "53": 73, "54": 76, "55": 76, "56": 84, "57": 85, "58": 96, "59": 103, "64": 111, "65": 117, "70": 122, "71": 128, "76": 133, "81": 138, "86": 143, "87": 149, "88": 157, "89": 157, "90": 157, "96": 141, "144": 136, "102": 141, "108": 131, "114": 131, "120": 106, "126": 106}, "uri": "base.htm", "source_encoding": "ascii", "filename": "C:\\Users\\John\\test_dmp\\homepage\\templates/base.htm"}
__M_END_METADATA
"""
