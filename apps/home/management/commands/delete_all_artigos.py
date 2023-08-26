from django.core.management.base import BaseCommand

from apps.home.models import dw_artigos, dw_autor


class Command(BaseCommand):
    """
    Deleta todos os artigos.
    """

    help = 'Deleta todos os artigos.'

    def handle(self, *args, **kwargs):
        # Exclua todos os artigos.
        dw_artigos.objects.all().delete()
