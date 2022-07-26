# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.move"

    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('purchase_manager', 'Waiting for Purchase Manager'),
                                        ('ready_to_confirm', 'Ready to Confirm'),
                                        ('posted', 'Posted'),
                                        ('cancel', 'Cancelled'),
                                        ], string='Status', required=True, readonly=True, copy=False, tracking=True,
                             default='draft')

    need_purchase_approval = fields.Boolean('Need Purchase Approval', compute='_check_purchase_approval')

    @api.depends('line_ids', 'state', 'line_ids.purchase_line_id')
    def _check_purchase_approval(self):
        for move in self:
            move.need_purchase_approval = False
            purchase = move.line_ids.filtered(lambda line: line.purchase_line_id)
            if purchase and move.state == 'draft':
                move.need_purchase_approval = True

    def send_manager_approval(self):
        self.state = 'purchase_manager'

    def action_purchase_manager(self):
        self.state = 'ready_to_confirm'

    def action_post_new(self):
        self.action_post()