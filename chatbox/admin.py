from django.contrib import admin
from .models import ChatMessage
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(ChatMessage)
class ChatMessageAdmin(SummernoteModelAdmin):
    list_display = ("user", "message", "created_on")
    search_fields = ("user__username", "message")
    list_filter = ("created_on",)
    summernote_fields = ("message",)

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")