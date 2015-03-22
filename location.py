# This file is part stock_warehouse_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['StockLocationResUser']
__metaclass__ = PoolMeta


class StockLocationResUser(ModelSQL):
    'Stock Location - Res User'
    __name__ = 'stock.location-res.user'
    _table = 'stock_location_res_user'
    location = fields.Many2One('stock.location', 'Location', ondelete='CASCADE',
        select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        required=True)
