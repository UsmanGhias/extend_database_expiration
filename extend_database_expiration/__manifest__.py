# -*- coding: utf-8 -*-
{
    'name': "Extend Database Expiry Date",
    'summary': "Automatically extend the expiration date of your Odoo database.",
    'description': """
        This module extends the expiration date of an Odoo Enterprise database automatically by one month, aimed at helping manage demo or development environments without the need for manual intervention.
    """,
    'author': "Usman Ghias",
    'website': "https://www.codcrafters.org",
    'category': 'Tools',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'price': 25.00,
    'currency': 'USD',
    'images': ['static/description/banner.png'],  # Ensure you have a banner.png in static/description
    'depends': ['base'],
    'data': [
        'data/ir_cron.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
