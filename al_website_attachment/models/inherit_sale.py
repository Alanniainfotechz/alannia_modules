# -*- coding: utf-8 -*-

from odoo import api,fields, models,_
import os

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attach_count = fields.Integer('Attachments')

    def get_view_attachents(self):
        print('slaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',self)
        attach_id = self.env['ir.attachment'].search([('res_id','=', self.id),('res_model','=','sale.order')])
        print('ggggggggggggggggggggggggggggggggggggggggggggggggg',attach_id)
        if attach_id:
            count = 0
            for attach in attach_id:
                count += 1
                print('11111111111111111111111111111',count)
            self.attach_count = count
            print('ttttttttttttttttttttttttttttttt',self.attach_count)
            return attach_id







    def view_attachments(self):
        attach_id = self.env['ir.attachment'].search([('res_id','=', self.id),('res_model','=','sale.order')])
        print('arrrrrrrrrrrrrrrrrrrrrrrrr',attach_id)
        print('viewwwwwwwwwwwwwwwww attachmentsssss',self)
        return {
            'name': _('View Website Attachments'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'ir.attachment',
            'domain': [('id', 'in', attach_id.ids)],
            'target': 'current',
        }

