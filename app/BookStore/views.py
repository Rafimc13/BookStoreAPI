from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer, BookCreateSerializer
from django.shortcuts import get_object_or_404


def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author}, safe=False)


@api_view(['POST'])
def create_book(request):
    serializer = BookCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



