from django.db import models
from datetime import timedelta
from django.utils import timezone


class AliasManager(models.Manager):
    def create_alias(self, alias, target, start=timezone.now(), end=None):
        """Function creates alias and validates"""
        objects = self.filter(alias=alias, target=target)
        if objects:
            "check if any aliases exists in this timeframe"
            for obj in objects:
                if obj.end:
                    if obj.start <= start < obj.end:
                        raise Exception(
                            "Cannot create alias: the same alias exists in the timeframe"
                        )
                else:
                    if obj.start <= start:
                        raise Exception(
                            "Cannot create alias: the same alias exists in the timeframe"
                        )

        if end and start and end < start:
            "Check if start less than end "
            raise Exception("Cannot create alias: timeframe doesn`t exist")
        alias = self.create(alias=alias, target=target, start=start, end=end)
        return alias

    def alias_replace(self, existing_alias, replace_at, new_alias_value):
        """fucntion stops existing_alias at replace_at moment,
           and creates alias with new_alias_value and start=replace_at"""
        if existing_alias.end:
            if not (existing_alias.start <= replace_at <= existing_alias.end):
                raise Exception(
                    "Cannot replace: replace_at moment doesn`t belong to an existing alias"
                )
        existing_alias.end = replace_at
        target = existing_alias.target
        existing_alias.save()
        new_alias = self.create_alias(
            alias=new_alias_value, target=target, start=replace_at, end=None
        )
        return new_alias

    def get_aliases(self, target=None, start=None, end=None):
        """function return aliases on chosen target"""
        if start and end:
            return self.filter(target=target, start__gte=start, end__lte=end)
        elif start:
            return self.filter(target=target, start__gte=start)
        else:
            return self.filter(target=target)
