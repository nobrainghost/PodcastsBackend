from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Delete all tables ending with "_episodes" from the database'

    def handle(self, *args, **options):
        # Get the default database connection
        connection = connections['default']
        cursor = connection.cursor()

        # Get all table names from the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Identify tables that end with "episodes"
        tables_to_delete = [table[0] for table in tables if table[0].endswith('_episodes')]

        # Delete each identified table
        for table in tables_to_delete:
            try:
                cursor.execute(f"DROP TABLE IF EXISTS {table};")
                self.stdout.write(self.style.SUCCESS(f"Deleted table: {table}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error deleting table {table}: {e}"))

        # Commit changes
        connection.commit()
        cursor.close()
