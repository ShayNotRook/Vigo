from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create initial user status groups'
    
    def handle(self, *args, **kwargs):
        groups = ['bronze', 'silver', 'gold', 'platinum']
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            
            if created:
                self.stdout.write(f'Group "{group_name}" created.')
                
            else:
                self.stdout.write(f'Group "{group_name} already exists."')
            