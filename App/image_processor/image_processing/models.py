from django.db import models

class ProcessedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    processed_text = models.TextField(blank=True, null=True)