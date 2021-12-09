# -*- coding: utf-8 -*-
from odoo import http

# class Cricket(http.Controller):
#     @http.route('/cricket/cricket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cricket/cricket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cricket.listing', {
#             'root': '/cricket/cricket',
#             'objects': http.request.env['cricket.cricket'].search([]),
#         })

#     @http.route('/cricket/cricket/objects/<model("cricket.cricket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cricket.object', {
#             'object': obj
#         })