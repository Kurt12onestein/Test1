# -*- coding: utf-8 -*-
{
    'name': 'Website Preloader / Animated / Light Mode / Dark Mode',
    'summary': 'Website Preloader',
    'version': '1.0',
    "license": "AGPL-3",
    'description': "Website Preloader",
    'author': 'Utku Halis',
    'support': 'utkuhalis97@gmail.com',
    'category': 'Website',
    'website': "https://utkuhalis.com",
    'depends': ['web', 'website'],
    'price': 0,
    'currency': 'EUR',
    'data': [
      "views/website.xml",
      "views/templates.xml",
    ],
    'images' : [
      'images/cover.png',
      'static/description/icon.png'
    ],
    'assets': {
      "web.assets_frontend": [
        "website_preloader/static/src/css/preloader.css",
        "website_preloader/static/src/js/preloader.js",
      ]
    },
    'installable': True,
    'auto_install': False,
}
