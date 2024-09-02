from django.core.exceptions import ValidationError
from django.db import models

from django.utils import timezone


class Entry(models.Model):
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        if len(self.content.split()) > 200:
            raise ValidationError('Content cannot exceed 200 words.')
