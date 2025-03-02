from django.db import models


class Document(models.Model):
    TEXT = 'text'
    PDF = 'pdf'
    EPUB = 'epub'

    TYPE_CHOICES = [
        (TEXT, 'Text'),
        (PDF, 'PDF'),
        (EPUB, 'EPUB'),
    ]

    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    doc_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=TEXT)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Document {self.id}"
