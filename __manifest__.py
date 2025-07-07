#Bruno Sacchetti - Prueba Tecnica

{
    'name': 'Aden Prueba Tecnica',
    'version': '1.0',
    'summary': 'Gestion de alumnos y programas',
    'description': 'Módulo para manejar alumnos, programas e inscripciones',
    'author': 'Bruno Sacchetti',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/alumno_views.xml',
        'views/programa_views.xml',
        'views/inscripcion_views.xml',
        'views/menu.xml',
    ],
    'application': True,
}
