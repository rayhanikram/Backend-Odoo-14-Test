# -*- coding: utf-8 -*-
{
    'name': "product_material_custom",

    'summary': """
        Backend Odoo Test 14""",

    'description': """
        Backend Odoo Test 14
    """,

    'author': "Rayhan Ikram Al Aziz",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_material.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
