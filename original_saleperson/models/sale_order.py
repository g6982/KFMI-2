from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    """ Add Original SalesPerson On Quotation"""

    original_employee_id = fields.Many2one(comodel_name='hr.employee', string='Original Sale Person')

    def _create_invoices(self, grouped=False, final=False, date=None):
        invoice = super(SaleOrderInherit, self)._create_invoices(grouped, final, date)
        invoice.write({'original_employee_id': self.original_employee_id.id})
        return invoice
