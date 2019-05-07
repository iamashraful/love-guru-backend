from django.db import models
from fast_drf.mixins.expose_api_model_mixin import ExposeApiModelMixin

__author__ = 'Ashraful'


class BaseEntity(models.Model, ExposeApiModelMixin):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        app_label = 'api'
