from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Find models with names containing specific keywords'

    def handle(self, *args, **options):
        app_label = 'core'  # Replace with your app label
        models = apps.get_app_config(app_label).get_models()

        filtered_models = [model for model in models if ('arts' in model.__name__.lower() and 'unitedstates' in model.__name__.lower()) or ('arts' in model.__name__.lower() and 'greatbritain' in model.__name__.lower())]

        for model in filtered_models:
            print(model.__name__)
