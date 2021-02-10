from django.db import models
from django.utils import timezone
from .manager import AliasManager


class Alias(models.Model):
    alias = models.CharField(max_length=100)
    target = models.CharField(max_length=24)
    start = models.DateTimeField(null=True, default=timezone.now())
    end = models.DateTimeField(null=True)
    objects = AliasManager()

    def __str__(self):
        return "{0} target:{1} from=<{2}> to=<{3}>".format(
            self.alias, self.target, self.start, self.end
        )
