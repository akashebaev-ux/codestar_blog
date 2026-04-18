from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration for the about app.
    **Attributes**
    ``default_auto_field``
        The default field type for auto-generated primary keys.
    ``name``
        The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
