import uuid
from django.db import models



class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Author Name", max_length=50)
    nationality = models.CharField("Nationality", max_length=50)
    birth_year = models.DateField(null=True, blank=True, editable=True)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        "Book Name",
        max_length=50,
    )
    author = models.ForeignKey(Author, on_delete = models.CASCADE, max_length=50)
    gener = models.CharField("Gener", max_length=50, null=True, blank=True)
    publication_year = models.DateField(null=True, blank=True, editable=True)
    book_img = models.ImageField(
        "Book Image", null=True, blank=True, help_text="Provide a book image.",upload_to='media/images/'
    )
    description = models.CharField(
        "Description",
        null=True,
        blank=True,
        max_length=200,
        help_text="Provide a short summary of this book",
    )

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"



