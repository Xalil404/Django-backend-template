from django.apps import AppConfig

class ProfileAPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProfileAPI'

    def ready(self):
        import ProfileAPI.signals
