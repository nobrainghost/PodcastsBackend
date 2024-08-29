# core/management/commands/populate_aggregated_data.py
import os
import django
import json
from django.core.management.base import BaseCommand
from django.apps import apps
from rest_framework.serializers import ModelSerializer
from core.models import AggregatedArts, AggregatedBusiness, AggregatedComedy, AggregatedPolitics, AggregatedHistory, AggregatedScience, AggregatedReligion, AggregatedLeisure, AggregatedSports

class Command(BaseCommand):
    help = 'Populate aggregated models with data from multiple tables'

    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poscastsbackend.settings')  # Replace with your project settings
        django.setup()

        # Define your categories and corresponding model classes
        categories = {
            'Arts': AggregatedArts,
            'Business': AggregatedBusiness,
            'Comedy': AggregatedComedy,
            'Politics': AggregatedPolitics,
            'History': AggregatedHistory,
            'Science': AggregatedScience,
            'Religion': AggregatedReligion,
            'Leisure': AggregatedLeisure,
            'Sports': AggregatedSports,
        }

        app_config = apps.get_app_config('core')

        for category, aggregated_model in categories.items():
            # Clear existing data for the category
            aggregated_model.objects.all().delete()

            # Get models that match the category name
            category_models = [model for model in app_config.get_models() if category.lower() in model.__name__.lower()]

            def get_serializer(model_class):
                """
                Create a serializer class for the given model class.
                """
                class DynamicSerializer(ModelSerializer):
                    class Meta:
                        model = model_class
                        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']
                return DynamicSerializer

            def serialize_and_save(models, category, aggregated_model):
                """
                Serialize and save data from the given models with the specified category.
                """
                for model in models:
                    try:
                        queryset = model.objects.all()
                        serializer_class = get_serializer(model)
                        serializer = serializer_class(queryset, many=True)
                        data = json.dumps(serializer.data)  # Convert data to JSON string

                        # Create aggregated model object
                        aggregated_model.objects.create(category=category, data=data)
                        print(f"Successfully processed model {model.__name__} for category {category}")
                    except Exception as e:
                        print(f"Error processing model {model.__name__} for category {category}: {e}")

            # Serialize and save data for the current category
            serialize_and_save(category_models, category, aggregated_model)

        self.stdout.write(self.style.SUCCESS('Successfully populated all aggregated models.'))

