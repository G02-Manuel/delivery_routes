from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_route_id = fields.Many2one('delivery.routes', string='Ruta de entrega')