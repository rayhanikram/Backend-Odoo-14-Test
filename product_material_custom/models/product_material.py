from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductMaterial(models.Model):
    _name = 'product.material'
    _description = 'Product Material'

    code = fields.Char(string='Material Code', required=True)
    name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True, default='fabric')
    buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Material Price must at least 100.')
