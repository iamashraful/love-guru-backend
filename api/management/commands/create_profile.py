from django.contrib.auth.models import User
from django.core.management import BaseCommand

from api.models import Profile


class Command(BaseCommand):
    def get_username_and_password(self):
        _username = input('Username --> ')
        _password = input('Password --> ')
        return _username, _password

    def create_user(self):
        print('Creating profile...')
        _u, _p = self.get_username_and_password()
        user, _created = User.objects.get_or_create(username=_u)
        user.set_password(_p)
        user.save()
        Profile.objects.get_or_create(name=_u, user_id=user.pk)
        print('Created.')

    def handle(self, *args, **options):
        self.create_user()
