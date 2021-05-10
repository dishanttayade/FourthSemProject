from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'user_profile'

    def ready(self):
        import user_profile.signals