# Generated by Django 4.2.11 on 2024-03-15 18:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("author", models.CharField(max_length=50, verbose_name="Authon Name")),
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
                        upload_to="",
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
            ],
        ),
    ]
