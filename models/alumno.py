from odoo import api, fields, models

class Alumno(models.Model):
    _name = 'aden.alumno'
    _description = 'Alumno'

    # Campos requeridos para la clase Alumno
    nombre = fields.Char(required=True)
    apellido = fields.Char(required=True)
    fecha_nacimiento = fields.Date()
    numero_legajo = fields.Char()
    email = fields.Char()
    telefono = fields.Char()
    direccion = fields.Text()

    # Pais no hace falta crearlo, ya que odoo tiene paises precargados, con el id lo identificamos
    pais_id = fields.Many2one('res.country', string='País')

    # Crea un campo calculado, que muestra el nombre completo del alumno
    # Se actualiza automáticamente cuando cambian el nombre o apellido
    name = fields.Char(string='Nombre Completo', compute='_compute_name', store=True)

    # Este metodo se ejecuta cada vez que cambia alguno de los 2 campos
    @api.depends('nombre', 'apellido')
    def _compute_name(self):
        for record in self:
            record.name = f'{record.nombre} {record.apellido}'