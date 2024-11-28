from typing import Type, List

from pydantic import BaseModel

import models
from mapper.base_profile import BaseProfile

class OrdersProfile(BaseProfile):
    exclude = []

    def __init__(self, dst_type: Type[BaseModel]):
        self.dst_type = dst_type

    def map(self, data: models.Orders):
        significant_vars = self._get_significant_vars(data)
        products_dto = self.dst_type(**significant_vars)
        return products_dto

    def map_list(self, data: List[models.Orders]):
        return [self.map(item) for item in data]

    #Tässä jouduin laittamaan manuaalisesti, koska en muuten saanut toimimaan.
    def _get_significant_vars(self, data):
        significant_vars = {
            'id': data.Id,
            'created_date': data.CreatedDate,
            'state': data.State,
            'customer_id': data.CustomerId,
            'confirmed_date': data.ConfirmedDate,
            'removed_date': data.RemovedDate,
            'handler_id': data.HandlerId,
        }
        return {k: v for k, v in significant_vars.items() if v is not None}

