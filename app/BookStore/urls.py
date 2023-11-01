from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:book_id>/', views.get_book),
    path('create/', views.create_book, name='create_book'),
]