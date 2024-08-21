from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    route_id = fields.Many2one('delivery.routes', string='Ruta')
    
    @api.onchange('partner_id')
    def compute_route(self):
        for record in self:
            record.route_id = record.partner_id.delivery_route_id
