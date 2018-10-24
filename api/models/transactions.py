from django.db import models

from api.models import BaseEntity

__author__ = 'Ashraful'


class Category(BaseEntity):
    name = models.CharField(max_length=32)

    class Meta:
        app_label = 'api'


class Wallet(BaseEntity):
    name = models.CharField(max_length=64)
    balance = models.FloatField(default=0)
    initial_balance = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'api'


class Transaction(BaseEntity):
    name = models.CharField(max_length=64)
    note = models.TextField(null=True, blank=True)
    category = models.ForeignKey('api.Category', on_delete=models.SET_NULL, null=True)
    wallet = models.ForeignKey('api.Wallet', on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(default=None, null=True)
    transaction_time = models.BigIntegerField(default=None, null=True)

    class Meta:
        app_label = 'api'
