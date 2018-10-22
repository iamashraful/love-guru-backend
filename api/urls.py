from django.urls import path

from api.views.users.auth_views import LoginView
from api.views.users.profile_view import ProfileListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='api_login_view'),
    path('profiles/', ProfileListView.as_view(), name='profile_list_view')
]
