from django.apps import AppConfig


class AdminbaliConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appart'

    def ready(self):
        import appart.signals
