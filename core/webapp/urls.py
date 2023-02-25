from django.urls import path
from webapp.views.add_book import add_book
from webapp.views.book_view import view
from webapp.views.delete_book import delete_book
from webapp.views.update_book import update_book

urlpatterns = [
    path('', view, name='home'),
    path('book/add/', add_book, name='add_book'),
    path('book/update/<int:pk>', update_book, name='update_book'),
    path('book/delete/<int:pk>', delete_book, name='delete_book')
]
