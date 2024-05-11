# Generated by Django 4.2.11 on 2024-05-01 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "author_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Author Name")),
                (
                    "nationality",
                    models.CharField(max_length=50, verbose_name="Nationality"),
                ),
                ("birth_year", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "book_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Book Name")),
                (
                    "gener",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Gener"
                    ),
                ),
                ("publication_year", models.DateField(blank=True, null=True)),
                (
                    "book_img",
                    models.ImageField(
                        blank=True,
                        help_text="Provide a book image.",
                        null=True,
                        upload_to="media/images/",
                        verbose_name="Book Image",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Provide a short summary of this book",
                        max_length=200,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lsmapp.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "loan_id",
                    models.URLField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("loan_date", models.DateField()),
                ("return_date", models.DateField()),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lsmapp.book"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Borrower",
                    ),
                ),
            ],
        ),
    ]
