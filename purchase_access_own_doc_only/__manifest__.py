# -*- coding: utf-8 -*-
{
    'name': "Purchase Own Doc. Access",

    'summary': """
        Purchase Own document access.""",

    'description': """
       Purchase Order own document access.
    """,

    # for the full list
    'category': 'Inventory/Purchase',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase','l10n_in_purchase', 'l10n_in', 'base_vat'],

    # always loaded
    'data': [
        'security/security_data.xml',
        'security/ir.model.access.csv',
    ],
}
