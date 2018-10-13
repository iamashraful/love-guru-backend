from django.urls import path

from api.views.users.profile_view import ProfileListView

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profile_list_view')
]
