from odoo import api, fields, models
from odoo.tools.populate import compute


class Programa(models.Model):
    _name = 'aden.programa'
    _description = 'Programa'

    # Campos requeridos para la clase Programa
    nombre = fields.Char(required=True)
    descripcion = fields.Text()

    # Crea un campo calculado, que muestra el nombre del programa
    # Se actualiza automáticamente cuando cambia el nombre
    name = fields.Char(string='Nombre del Programa', compute='_compute_name', store=True)

    # Este metodo se ejecuta cada vez que cambia el campo nombre
    @api.depends('nombre')
    def _compute_name(self):
        for record in self:
            record.name = record.nombre