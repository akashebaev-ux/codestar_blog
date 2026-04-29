from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage


@login_required
def chat(request):
    room, created = ChatRoom.objects.get_or_create(name="General")

    if request.method == "POST":
        ChatMessage.objects.create(
            room=room,
            user=request.user,
            message=request.POST.get("message")
        )
        return redirect("chat")

    chat_messages = ChatMessage.objects.filter(room=room)

    return render(request, "chat.html", {
        "room": room,
        "chat_messages": chat_messages
    })


