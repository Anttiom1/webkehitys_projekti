import inspect
from typing import Type, List

from pydantic import BaseModel

import models
from mapper.base_profile import BaseProfile


class ProductsProfile(BaseProfile):
    exclude = []

    def __init__(self, dst_type: Type[BaseModel]):
        self.dst_type = dst_type

    def map(self, data: models.Products):
        significant_vars = self._get_significant_vars(data)
        products_dto = self.dst_type(**significant_vars)
        return products_dto

    def map_list(self, data: List[models.Products]):
        return [self.map(item) for item in data]

    def _get_significant_vars(self, data):
        significant_vars = {}
        for key, value in vars(data).items():
            # Convert PascalCase to snake_case
            normalized_key = ''.join(['_' + i.lower() if i.isupper() else i for i in key]).lstrip('_')
            if normalized_key not in self.exclude:
                significant_vars[normalized_key] = value
        return significant_vars
