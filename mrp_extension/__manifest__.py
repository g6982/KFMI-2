# -*- coding: utf-8 -*-
{
    'name': "mrp_extension",

    'summary': """
        Custimazation of mrp module""",

    'description': """
       Customisation of mrp module by adding some fields on reports and added the balanced qty
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','hr'],

    # always loaded
    'data': [
        'data/customized_record_rules.xml',
        'security/ir.model.access.csv',
        'views/mrp_view.xml',
    ],
}
