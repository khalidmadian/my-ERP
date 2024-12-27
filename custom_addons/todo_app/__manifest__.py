# -*- coding: utf-8 -*-
{
    'name': "To-Do App",
    'summary': """""",
    "license": "",
    'description': """""",
    'author': "",
    'website': "",
    'category': '',
    'version': '0.1',

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'reports/sicli_invoice_report.xml',
    ],

    'installable': True,
    'application': True,
}
