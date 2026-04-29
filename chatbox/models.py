from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatMessage(models.Model):
    """
    Stores a single chat message entry related to :model:`auth.User`.
    """
    room = models.ForeignKey("ChatRoom", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}"
    

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name