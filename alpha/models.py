from django.db import models

class Editor(models.Model):
    Location = models.CharField(max_length=30)
    Timeshot = models.CharField(max_length=30)
    Details = models.CharField(max_length=30)
