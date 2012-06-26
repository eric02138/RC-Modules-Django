from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)
    help_text = models.CharField(max_length=1000)
    updated = models.DateTimeField()
    whatis = models.CharField(max_length=200)
    
