from odoo import models, fields


class DeliveryRoutes(models.Model):
    _name = 'delivery.routes'
    _rec_name = 'name'
    _description = 'Routes for deliveries'

    name = fields.Char(string='Nombre', required=True)
    country_id = fields.Many2one('res.country', string='País')
    state_ids = fields.Many2many('res.country.state', string='Provincias')
