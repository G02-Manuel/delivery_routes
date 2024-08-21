from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    route_id = fields.Many2one('delivery.routes', string='Ruta')
    
    @api.model
    def create(self, vals):
        # Verificar si la orden de venta está en los valores
        if 'origin' in vals and vals['origin']:
            sale_order = self.env['sale.order'].search([('name', '=', vals['origin'])], limit=1)
            if sale_order and sale_order.route_id:
                vals['route_id'] = sale_order.route_id.id
        return super(StockPicking, self).create(vals)
