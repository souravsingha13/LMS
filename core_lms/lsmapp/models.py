import uuid
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

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
    author = models.ForeignKey(Author, on_delete=models.CASCADE, max_length=50)
    gener = models.CharField("Gener", max_length=50, null=True, blank=True)
    publication_year = models.DateField(null=True, blank=True, editable=True)
    book_img = models.ImageField(
        "Book Image",
        null=True,
        blank=True,
        help_text="Provide a book image.",
        upload_to="media/images/",
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


class Loan(models.Model):
    loan_id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Borrower")
    loan_date = models.DateField(null = False, blank = False)
    return_date = models.DateField(null = False, blank = False)

    def __str__(self):
        return f"Loan ID: {self.loan_id}, Book: {self.book}, User: {self.user}, Loan Date: {self.loan_date}, Return Date: {self.return_date}"
