# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mrp_extension(models.Model):
    _inherit = 'mrp.workcenter'

    allowed_user = fields.Many2many('res.users',string='Allowed User')


class MrpWorkcenterProductivityInherit(models.Model):
    _inherit = "mrp.workcenter.productivity"

    employee_id = fields.Many2one('hr.employee',string='Employee')

class MrpWorkOrder(models.Model):
    _inherit = "mrp.workorder"

    part_quantities_line = fields.One2many('part.quantity','part_qty_id',string='Part Qty')
    work_balanced_qty = fields.Integer(string='Balanced Qty', compute='work_compute_balanced_qty',store=True)
    work_finished_qty = fields.Integer(string='Finished Qty',compute='work_compute_balanced_qty',store=True)
    work_original_qty =  fields.Float(related='production_id.product_qty',store=True)

    @api.depends('part_quantities_line')
    def work_compute_balanced_qty(self):
        for rec in self:
            rec.work_finished_qty = sum(self.part_quantities_line.mapped('finished_qty'))
            rec.work_balanced_qty = rec.work_original_qty - rec.work_finished_qty

class MrpPartQty(models.Model):
    _name='part.quantity'
    _description='Part quantity'

    part_qty_date = fields.Date(string='Part Qty')
    finished_qty = fields.Integer(string='Finished Qty')
    machine_name =  fields.Char(string='Machine Name')
    balanced_qty =  fields.Integer(string='Balanced Qty', compute='compute_balanced_qty',store=True)
    part_qty_id = fields.Many2one('mrp.workorder', string='Order Reference', required=True, ondelete='cascade', index=True, copy=False)

    @api.depends('finished_qty')
    def compute_balanced_qty(self):
        for rec in self:
            # import pdb;pdb.set_trace()
            if rec.finished_qty and self.env.context.get('is_calculated'):
                rec.balanced_qty = rec.part_qty_id.production_id.product_qty - sum((self.part_qty_id.part_quantities_line-rec).mapped('finished_qty'))

            # if rec.finished_qty:
            #     balanced_qty =  len(self.part_qty_id.part_quantities_line)>1 and rec.part_qty_id.production_id.work_balance_qty or rec.part_qty_id.production_id.product_qty
            #     rec.balanced_qty = balanced_qty - rec.finished_qty
            #     rec.part_qty_id.production_id.work_balance_qty = rec.balanced_qty
