from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestProductMaterial(TransactionCase):


    def setUp(self):
        super(TestProductMaterial, self).setUp()
        self.supplier_id = self.env['res.partner'].create({
            'name': 'Supplier 1'
        })

    def test_create_material(self):
        material = self.env['product.material'].create({
            'code': 'FB001',
            'name': 'Linen',
            'material_type': 'fabric',
            'buy_price': 150000,
            'supplier_id': self.supplier_id.id
        })
        self.assertEqual(material.name, 'Linen')

    # error test buy price
    def test_material_price_validation(self):
        with self.assertRaises(ValidationError):
            self.env['product.material'].create({
                'code': 'CTN001',
                'name': 'Popelin',
                'material_type': 'cotton',
                'buy_price': 50, 
                'supplier_id': self.supplier_id.id
            })

    def test_update_material(self):
        material = self.env['product.material'].create({
            'code': 'JNS001',
            'name': 'Updatable Material',
            'material_type': 'jeans',
            'buy_price': 200000,
            'supplier_id': self.supplier_id.id
        })
        material.write({
            'name': 'Blue Jeans'
        })
        self.assertEqual(material.name, 'Blue Jeans')

    def test_delete_material(self):
        material = self.env['product.material'].create({
            'code': 'FB002',
            'name': 'Deletable Material',
            'material_type': 'fabric',
            'buy_price': 250000,
            'supplier_id': self.supplier_id.id
        })
        material_id = material.id
        material.unlink()
        self.assertFalse(self.env['product.material'].search([('id', '=', material_id)]))
