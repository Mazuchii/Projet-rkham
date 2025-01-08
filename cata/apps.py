from django.apps import AppConfig

class CataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cata'

    def ready(self):
        # Import here to avoid "Apps aren't loaded yet" error
        from django.contrib.auth.models import User
        # Place signal registrations or other necessary imports here
