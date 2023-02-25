from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import GuessBook
from webapp.forms import BookForms
from django.core.handlers.wsgi import WSGIRequest


def update_book(request: WSGIRequest, pk):
    books = get_object_or_404(GuessBook, pk=pk)
    if request.method == 'POST':
        form = BookForms(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'update_book.html', context={'form': form})
    form = BookForms(instance=books)
    return render(request, 'update_book.html', context={'form': form})
