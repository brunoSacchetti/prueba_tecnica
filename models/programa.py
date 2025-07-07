from odoo import api, fields, models
from odoo.tools.populate import compute


class Programa(models.Model):
    _name = 'aden.programa'
    _description = 'Programa'

    # Campos requeridos para la clase Programa
    nombre = fields.Char(required=True)
    descripcion = fields.Text()

    name = fields.Char(string='Nombre del Programa', compute='_compute_name', store=True)

    @api.depends('nombre')
    def _compute_name(self):
        for record in self:
            record.name = record.nombre