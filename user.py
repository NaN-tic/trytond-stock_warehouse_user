# This file is part stock_warehouse_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['User']
__metaclass__ = PoolMeta


class User:
    __name__ = "res.user"
    warehouses = fields.Many2Many('stock.location-res.user', 'user', 'location',
        'Warehouses', domain=[
            ('type', '=', 'warehouse'),
        ],
        help='Warehouses the user can work')
    warehouse = fields.Many2One('stock.location', 'Warehouse', domain=[
        ('id', 'in', Eval('warehouses', [])),
        ], depends=['warehouses'],
        help='Current warehouse the user are working')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._preferences_fields.extend([
                'warehouse',
                'warehouses',
                ])
        cls._context_fields.insert(0, 'warehouse')
        cls._context_fields.insert(0, 'warehouses')

    def get_status_bar(self, name):
        status = super(User, self).get_status_bar(name)
        if self.warehouse:
            status += ' - %s' % (self.warehouse.rec_name)
        return status
