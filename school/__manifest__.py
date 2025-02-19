
{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'author': 'ODOO17',
    'data': [
        'views/view_school_student.xml',
        'views/view_school_faculty.xml',
        'views/result_view.xml',
        'wizards/create_appointment.xml',
        'views/admin_view.xml',
        'views/std_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir.sequence.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
'test': [
        'tests/test_faculty.py',
    ],
}
