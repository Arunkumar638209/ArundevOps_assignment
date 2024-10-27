# library/models.py

from django.db import models

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='ebooks/')
    
    def __str__(self):
        return self.title

