#This file is part stock_warehouse_user module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .location import *
from .user import *

def register():
    Pool.register(
        StockLocationResUser,
        User,
        module='stock_warehouse_user', type_='model')
