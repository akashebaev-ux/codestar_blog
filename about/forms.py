from django import forms 
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Form for submitting a collaboration request related to :model:`about.CollaborateRequest`.
    **Fields**
    ``name``
        The name of the person submitting the request.
    ``email``
        The email address of the person submitting the request.
    ``message``
        The message content of the collaboration request.
    """

    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message",)