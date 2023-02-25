from django.shortcuts import render
from webapp.models import GuessBook
from django.core.handlers.wsgi import WSGIRequest


def view(request: WSGIRequest):
    books = GuessBook.objects.exclude(status='Blocked').order_by('-created_at')
    context = {'books': books}
    return render(request, 'home.html', context=context)
