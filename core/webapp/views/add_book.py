from django.shortcuts import render, redirect
from webapp.models import GuessBook
from webapp.forms import BookForms
from django.core.handlers.wsgi import WSGIRequest


def add_book(request: WSGIRequest):
    if request.method == "GET":
        form = BookForms()
        return render(request, 'add_book.html', context={'form': form})

    form = BookForms(data=request.POST)
    if form.is_valid():
        GuessBook.objects.create(**form.cleaned_data)
        return redirect('home')
    else:
        return render(request, 'add_book.html', context={'form': form})
