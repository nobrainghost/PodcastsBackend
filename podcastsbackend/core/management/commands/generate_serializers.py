import os
import django
from django.core.management.base import BaseCommand
from django.apps import apps
from rest_framework import serializers

class Command(BaseCommand):
    help = 'Generate serializers for all models in a specified app'

    def handle(self, *args, **options):
        # Set up Django environment
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace with your project settings
        django.setup()
        
        app_label = 'core'  # Replace with your app label
        
        # Get all models from the app
        models = apps.get_app_config(app_label).get_models()

        # Generate serializers.py file
        serializers_path = os.path.join('core', 'serializers.py')  # Replace with your app path
        with open(serializers_path, 'w') as f:
            f.write('from rest_framework import serializers\n')
            f.write('from .models import *\n\n')  # Import all models
            
            for model in models:
                model_name = model.__name__
                fields = [field.name for field in model._meta.get_fields() if field.name != 'id']  # Exclude 'id' if needed
                
                # Write serializer class to file
                f.write(f'class {model_name}Serializer(serializers.ModelSerializer):\n')
                f.write(f'    class Meta:\n')
                f.write(f'        model = {model_name}\n')
                f.write(f'        fields = {fields}\n\n')

        self.stdout.write(self.style.SUCCESS('Successfully generated serializers.'))
