from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import GuessBook
from django.core.handlers.wsgi import WSGIRequest


def delete_book(request: WSGIRequest, pk):
    book = get_object_or_404(GuessBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_book.html', context={'book': book})
    if request.method == 'POST':
        book.delete()
    return redirect('home')
