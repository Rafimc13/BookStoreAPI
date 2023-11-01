from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "author", "public_year", "ISBN", "genre"]

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
