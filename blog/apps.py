from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration for the blog app.
    **Attributes**
    ``default_auto_field``
        The default field type for auto-generated primary keys.
    ``name``
        The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
