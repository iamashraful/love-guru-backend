from django.db import models

from common.enums import GenderEnum
from common.models.base import BaseEntity


class Profile(BaseEntity):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=42)

    class Meta:
        app_label = 'common'

    def __str__(self):
        return self.name


class ProfileMeta(BaseEntity):
    phone = models.CharField(max_length=16, null=True)
    address = models.TextField(null=True)
    gender = models.CharField(default=GenderEnum.Male.value)
    photo = models.ImageField(null=True)

    class Meta:
        app_label = 'common'
