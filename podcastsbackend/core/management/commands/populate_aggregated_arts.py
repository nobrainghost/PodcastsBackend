# core/management/commands/populate_aggregated_data.py
import os
import json
import django
from django.core.management.base import BaseCommand
from django.apps import apps
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer
from core.models import AggregatedArts

class Command(BaseCommand):
    help = 'Populate AggregatedArts model with data from multiple tables'

    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poscastsbackend.settings')  # Replace with your project settings
        django.setup()

        # Get models with specific keywords in their names
        arts_models = [model for model in apps.get_app_config('core').get_models() if 'arts' in model.__name__.lower()]
        united_states_models = [model for model in apps.get_app_config('core').get_models() if 'united states' in model.__name__.lower()]
        great_britain_models = [model for model in apps.get_app_config('core').get_models() if 'great britain' in model.__name__.lower()]

        # Clear existing data
        AggregatedArts.objects.all().delete()

        def get_serializer(model_class):
            class DynamicSerializer(ModelSerializer):
                class Meta:
                    model = model_class
                    fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']
            return DynamicSerializer

        def serialize_and_save(models, category):
            for model in models:
                try:
                    queryset = model.objects.all()
                    serializer_class = get_serializer(model)
                    serializer = serializer_class(queryset, many=True)
                    data = json.dumps(serializer.data)
                    AggregatedArts.objects.create(category=category, data=data)
                except Exception as e:
                    print(f"Error processing model {model.__name__}: {e}")

        # Serialize and save data for each category
        serialize_and_save(arts_models, 'Arts')
        serialize_and_save(united_states_models, 'United States')
        serialize_and_save(great_britain_models, 'Great Britain')

        self.stdout.write(self.style.SUCCESS('Successfully populated AggregatedArts model.'))
