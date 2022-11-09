# -*- coding:utf-8 -*-
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('user_id')
    def onchange_original_employee_id(self):
        user_id = self.env['hr.employee'].search([('user_id','=', self.user_id.id)], limit=1)
        if user_id:
            self.original_employee_id = user_id.id
        else:
            self.original_employee_id = False

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
