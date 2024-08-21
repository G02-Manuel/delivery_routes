from odoo import models, fields


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    route_id = fields.Many2one('delivery.routes', string='Ruta')
