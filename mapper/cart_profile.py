from typing import List, Type

from pydantic import BaseModel

import models


class CartProfile:
    exclude = []

    def __init__(self, dst_type: Type[BaseModel]):
        self.dst_type = dst_type

    def map(self, data: models.OrdersProducts):
        significant_vars = self._get_significant_vars(data)
        return self.dst_type(**significant_vars)

    def map_list(self, data: List[models.OrdersProducts]):
        return [self.map(item) for item in data]

    def _get_significant_vars(self, data):
        significant_vars = {
            'order_id': data.OrderId,
            'product_id': data.ProductId,
            'unit_count': data.UnitCount,
            'unit_price': data.UnitPrice,
        }
        return {k: v for k, v in significant_vars.items() if k not in self.exclude}
