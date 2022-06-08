from django.db import models

class GuessColor(models.Model):
    parameter = models.CharField(max_length=200)