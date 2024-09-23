from odoo import models, fields, api
from odoo.exceptions import ValidationError


class POSOrderCustom(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create(self, vals):
        order = super(POSOrderCustom, self).create(vals)
        customer_email = order.partner_id.email
        if customer_email:
            template = self.env.ref('point_of_sale_custom.email_template_pos_receipt')
            self.env['mail.template'].browse(template.id).send_mail(order.id, force_send=True)
            order.note = 'Email sent to %s' % (customer_email)
        return order
    
class PosConfig(models.Model):
    _inherit = 'pos.config'


    
