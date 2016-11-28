#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Warmup Task 2"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """This will Calculate total cost of a quantity of items if already exist"""
    
    return {k: v * FRUIT[k] for k, v in shoplist.iteritems()
            if k in FRUIT}


def get_total_cost(shoplist):
    """This will return the total cost of quantities"""

    costs = get_cost_per_item(shoplist)
    return sum(costs.itervalues())
