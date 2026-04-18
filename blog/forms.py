from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment related to :model:`blog.Post` and :model:`auth.User`.
        **Fields**
        ``body``
            The text content of the comment.
    """
    class Meta:
        model = Comment
        fields = ("body",)