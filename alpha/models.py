from django.db import models

class Editor(models.Model):
    Location = models.CharField(max_length=30)
    Timeshot = models.CharField(max_length=30)
    Details = models.CharField(max_length=30)

class Location(models.Model):
    Location = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Timeshot(models.Model):
    Timeshot = models.CharField(max_length=30)

    def __str__(self):
        return self.Timeshot