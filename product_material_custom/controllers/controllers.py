# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ProductMaterialController(http.Controller):

    @http.route('/product_material_custom/materials', auth='user', type='json', methods=['GET'], csrf=False)
    def get_material(self, material_type=None):
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type))
        materials = request.env['product.material'].search_read(domain)
        return materials
    
    @http.route('/product_material_custom/material', auth='user', type='json', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        code = kwargs.get('code')
        name = kwargs.get('name')
        material_type = kwargs.get('material_type')
        buy_price = kwargs.get('buy_price')
        supplier_id = kwargs.get('supplier_id')

        if not all([code, name, material_type, buy_price, supplier_id]):
            return {'error': 'All fields are required.'}

        new_material = request.env['my_module.material'].create({
            'code': code,
            'name': name,
            'material_type': material_type,
            'buy_price': float(buy_price),
            'supplier_id': int(supplier_id),
        })
        return {'id': new_material.id, 'message': 'Material created successfully.'}
    

    @http.route('/product_material_custom/material/<int:material_id>', auth='user', type='json', methods=['PUT'], csrf=False)
    def update_material(self, material_id, **kwargs):
        material = request.env['product.material'].browse(material_id)
        if not material:
            return {'error': 'Material not found.'}

        material.write({
            'code': kwargs.get('material_code', material.code),
            'name': kwargs.get('material_name', material.name),
            'material_type': kwargs.get('material_type', material.material_type),
            'buy_price': float(kwargs.get('material_buy_price', material.buy_price)),
            'supplier_id': kwargs.get('supplier_id', material.supplier_id.id),
        })
        return {'message': 'Material updated successfully.'}

    @http.route('/product_material_custom/material/<int:material_id>', auth='user', type='json', methods=['DELETE'], csrf=False)
    def delete_material(self, material_id):
        material = request.env['product.material'].browse(material_id)
        if not material:
            return {'error': 'Material not found.'}

        material.unlink()
        return {'message': 'Material has been deleted.'}