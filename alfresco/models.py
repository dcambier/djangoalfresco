from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
 