# See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Price show only for Portal Users',
    'version': '15.0.1.0.0',
    'category': 'Partner',
    'license': 'AGPL-3',
    'author': 'Alanniainfotechz',
    'website': '',
    'price': 7.18,
    'currency': 'USD',
    'summary': 'This module helps to hide the website price for Public User',
    'depends': [
        'website_sale',
    ],
    'data': [
        'views/inherit_web_template.xml',

    ],
    'images':['static/description/cover_screenshot.png'],
    'installable': True,
    'auto_install': False,
}
