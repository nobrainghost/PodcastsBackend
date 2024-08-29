from django.core.management.base import BaseCommand
from django.apps import apps
from rest_framework import serializers

class Command(BaseCommand):
    help = 'Generate DRF serializers for all models in the specified app'

    def add_arguments(self, parser):
        parser.add_argument('core', type=str)

    def handle(self, *args, **kwargs):
        app_name = kwargs['core']
        app = apps.get_app_config(app_name)
        models = app.get_models()

        serializers_code = ''

        for model in models:
            model_name = model.__name__
            fields = {field.name: serializers.CharField() for field in model._meta.get_fields()}
            
            # Basic serializer definition
            serializer_code = f"""
class {model_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = {list(fields.keys())}
"""
            serializers_code += serializer_code

        # Output serializers code
        with open(f'{app_name}/serializers.py', 'w') as file:
            file.write(serializers_code)

        self.stdout.write(self.style.SUCCESS('Serializers have been generated successfully.'))
