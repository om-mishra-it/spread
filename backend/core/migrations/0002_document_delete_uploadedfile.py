# Generated by Django 5.1.5 on 2025-03-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255)),
                ("content", models.TextField(blank=True)),
                ("file", models.FileField(blank=True, null=True, upload_to="uploads/")),
                (
                    "doc_type",
                    models.CharField(
                        choices=[("text", "Text"), ("pdf", "PDF"), ("epub", "EPUB")],
                        default="text",
                        max_length=10,
                    ),
                ),
                ("processed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="UploadedFile",
        ),
    ]
