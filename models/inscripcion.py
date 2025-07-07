from odoo import api, fields, models

class Inscripcion(models.Model):
    _name = 'aden.inscripcion'
    _description = 'Inscripcion'

    # Campos requeridos para la clase Inscripcion
    # Relacion entre ALUMNO - PROGRAMA

    alumno_id = fields.Many2one('aden.alumno', string='Alumno', required=True)
    programa_id = fields.Many2one('aden.programa', string='Programa', required=True)