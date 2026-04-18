from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin view for :model:`blog.Post`.
    Displays the title, slug, status and created_on fields in the admin list view.
    Allows searching by title and content, and filtering by status and created_on.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)