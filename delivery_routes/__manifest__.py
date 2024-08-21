{
    'name': 'Rutas de entregas',
    'version': '1.0',
    'author': 'Gerlin Matos',
    'category': 'Contacts',
    'summary': 'Gestiona rutas y asócialas a contactos, órdenes de venta, picking y vehículos',
    'depends': ['base', 'contacts', 'sale', 'stock', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/routes_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/fleet_vehicle_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}