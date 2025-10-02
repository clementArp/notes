from django.shortcuts import render
from .models import Note


def home(request):
    notes = Note.objects.order_by("-created_at")[:20]
    return render(request, "notes/home.html", {"notes": notes})
