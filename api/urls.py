from django.urls import path
from fast_drf.router import BasicRouter

urlpatterns = BasicRouter.get_urls()
