# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright (c) 2022  - feddad.imad@gmail.com

{
    'name': "Algérie - 58 Wilaya d'algérie",
    'version': '24.1',
    'category': 'Accounting',
    'description': """
This is the module to manage the wilaya & commune for Algeria in Odoo.
========================================================================

This module applies to companies based in Algeria.
.

**Email:** feddad.imad@gmail.com
""",
    'author': 'feddad.imad@gmail.com',
    'depends': ['sale', 'contacts', 'base', 'base_address_extended'],
    'data': [
	    # 'security/ir.model.access.csv',
        'data/wilayas_data.xml',
        'data/data_res_city.xml',
        # 'views/res_commune.xml',
        'views/res_country_state.xml',
	    # 'views/res_partner.xml'
    ],
   'images': ['static/description/banner.gif'], 

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',

}

