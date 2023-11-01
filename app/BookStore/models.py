from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    public_year = models.IntegerField(max_length=10)
    ISBN = models.IntegerField(max_length=50)  # International Standard Book Number
    genre = models.CharField(max_length=100)

    def __str__(self):
        my_return = (f"Title of the book: {self.title}, Author: {self.author},"
                     f"Publication year: {self.public_year}")
        return my_return





