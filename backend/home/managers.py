from django.db import models
from django.db.models.aggregates import Sum


class PartQuerySet(models.QuerySet):
    def for_building(self, building_id):
        return self.filter(unit__surface__room__level__building__pk=building_id)

    def total_price(self):
        return self.aggregate(total_price=Sum('price'))
