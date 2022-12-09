from django.apps import AppConfig


class YarukikkakeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yarukikkake'
    
    def ready(self):
        from .scheduler import start
        start()
