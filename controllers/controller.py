from odoo import http
from odoo.http import request

class AdenController(http.Controller):

    @http.route('/api/programa/<int:programa_id>/alumnos', auth='public', type='http', methods=['GET'], csrf=False)
    def get_alumnos_por_programa(self, programa_id):
        inscripciones = request.env['aden.inscripcion'].sudo().search([
            ('programa_id', '=', programa_id)
        ])

        alumnos = []
        for inscripcion in inscripciones:
            alumno = inscripcion.alumno_id
            alumnos.append({
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'numero_legajo': alumno.numero_legajo,
                'email': alumno.email,
                'telefono': alumno.telefono,
                'pais': alumno.pais_id.name if alumno.pais_id else None
            })

        import json
        return request.make_response(
            json.dumps(alumnos),
            headers=[('Content-Type', 'application/json')]
        )
