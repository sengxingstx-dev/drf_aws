from django.db import models
from utils.file_utils import (
    custom_cover_image_filename,
    validate_image_extension,
    max_file_size_validator,
)


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(
        upload_to=custom_cover_image_filename,
        null=True,
        blank=True,
        validators=[validate_image_extension, max_file_size_validator],
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # one-to-many
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)  # one-to-one
    genre = models.ManyToManyField(Genre)  # many-to-many

    def __str__(self):
        return self.title


# Intermediate table for Many-to-Many relationship
# class BookGenre(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.book} - {(self.genre)}'
