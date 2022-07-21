# -*- coding: utf-8 -*-
{
    'name': "Sale Order Delivery Status",
    'summary': """Delivery Status on Sale Order""",
    'description': """This module adds Delivery Status on Sale Order""",

    'author': "Merveille ZEBAZE",
    'maintainer': 'Merveille ZEBAZE',
    'website': "http://merveillezebaze.pythonanywhere.com/",
    'category': 'Sales',
    'version': '0.1',
    'price':10,
    'currency': 'EUR',
    'depends': ['sale_stock', 'sale_management'],

    'data': ['views/sales_order.xml'],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
