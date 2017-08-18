from CBF.youtube_uploads import execute_import
from CBF.settings.local import DATA_DIR
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate sermons with youtube CBF account'

    def handle(self, *args, **options):
        execute_import(DATA_DIR)
