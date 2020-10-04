from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        print("total : ", total, type(total))
        if kwargs['admin']:
            is_superuser = True
            is_staff=True
        else:
            is_superuser = False
            is_staff=False
        
        for i in range(total):
            User.objects.create_user(
                first_name=get_random_string(),
                last_name=get_random_string(),
                username=get_random_string(), 
                email=get_random_string() + "@mail.com", 
                password='12345',
                is_superuser=is_superuser,
                is_staff=is_staff
            )
    
