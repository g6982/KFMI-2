from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class InvoiceInherit(models.Model):
    _inherit = 'account.move'

    original_employee_id = fields.Many2one(comodel_name='hr.employee', string='Original Sale Person')


class SaleAdvancePaymentInvInh(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        invoice = super(SaleAdvancePaymentInvInh,self)._create_invoice(order, so_line, amount)
        invoice.write({'original_employee_id': order.original_employee_id.id})
        return invoice
