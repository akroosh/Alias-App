from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from .models import Alias


class AliasTestCase(TestCase):
    def test_aliases(self):
        """Testing create_alias function"""
        # Create two different aliases with the same targets and
        # the same alias objects but second alias object starts when the first ends
        Alias.objects.create_alias(alias="test", target="test")
        Alias.objects.create_alias(
            alias="test alias", target="test", end=timezone.now() + timedelta(days=1)
        )
        tmp = Alias.objects.get(alias="test alias", target="test")
        Alias.objects.create_alias(alias="test_alias", target="test", start=tmp.end)
        # the same alias objects but with the different timeframes
        Alias.objects.create_alias(
            alias="test alias",
            target="test",
            start=timezone.now() - timedelta(days=10),
            end=timezone.now() - timedelta(days=3),
        )
        # the next one raise exception because of timeframe:
        # Alias.objects.create_alias(alias='test alias', target='test', start=timezone.now()-timedelta(days=7), end=timezone.now()-timedelta(days=3))

        """Testing get_aliases function"""
        result = Alias.objects.get_aliases(target="test")
        print(result)
        result1 = Alias.objects.get_aliases(
            target="test", start=timezone.now() - timedelta(days=11)
        )
        print(result1)
        result2 = Alias.objects.get_aliases(
            target="test",
            start=timezone.now() - timedelta(days=11),
            end=timezone.now() - timedelta(days=3),
        )
        print(result2)

        """Testing replace_at function"""
        result3 = Alias.objects.alias_replace(
            existing_alias=Alias.objects.get(alias="test"),
            replace_at=timezone.now() + timedelta(days=1),
            new_alias_value="new test",
        )
        print(result3)
        # the next one raise exception because existing alias doesn`t exist in this timeframe:
        # Alias.objects.alias_replace(existing_alias=Alias.objects.get(alias='test'),
        #  replace_at=timezone.now()-timedelta(days=1), new_alias_value='new test')
