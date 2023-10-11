from django.core.management.base import BaseCommand

from apps.home.models import dw_artigos


class Command(BaseCommand):
    """
    Deleta todos os artigos.
    """

    help = 'Deleta todos os artigos.'

    def handle(self, *args, **kwargs):
        dw_artigos.objects.all().delete()
