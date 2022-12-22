# -*- coding: utf-8 -*-
{
    'name': "Hospital managment test",
    'summary': """Hospital managment system""",
    'description': """Hospital managment system""",
    'category': 'Uncategorized',
    'sequence':-100,
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base','mail'],
    'data': [
        'views/menu.xml',
        'views/patient_view.xml',
        'security/ir.model.access.csv',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],

    'demo': [],
    'application' : True,
    'auto_install' : False,
}
