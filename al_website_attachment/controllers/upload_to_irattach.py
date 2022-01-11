# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import os
import base64
import io

class CreateWeb(http.Controller):

    @http.route(['/file/upload'], type='http', auth='user', website=True)
    def upload_document(self, redirect=None, **post):
        print('posssssssssssssssssssssssssssssssssssssssss',post)
        file = post.get('attachment')
        order_id = post.get('order_id')
        so_name = post.get('so_name')
        order = request.env['sale.order'].browse(int(order_id))
        user = request.env.user.partner_id
        attach_id = request.env['ir.attachment']
        if file:
            path = os.getcwd()
            new_path = '/tmp/drop_box'
            if not os.path.exists(new_path):
                os.mkdir(new_path, 0o777)
            name = post.get('attachment').filename
            file = post.get('attachment')
            attachment = file.read()

            if name:
                filepath = os.path.join(new_path, name)
                with open(filepath, 'wb') as file:
                    file.write(attachment)
                    file.close()
        # Attach to IR Attachment
            attachment_id = attach_id.create({
                'name': name,
                'type': 'binary',
                'datas': base64.b64encode(attachment),
                'res_model': 'sale.order',
                'res_name': so_name,
                'res_id': order.id
            })

            delete_record = os.remove(filepath)
        return request.redirect('/shop/cart')

    @http.route(['/file_upload/remove'], type='http', auth='user', csrf=False,
                website=True)
    def remove_document(self, redirect=None, **post):
        attach_id = int(post.get('attach_id'))
        print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',attach_id)
        del_id = request.env['ir.attachment'].browse(attach_id)
        print('dellllllllllllllllll',del_id)

        try:
            print('dekkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
            del_id.unlink()

        except:
            pass

        return request.redirect('/shop/cart')




