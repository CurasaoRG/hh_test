from django.db import models

class Equation(models.Model):
    parameter = models.CharField(max_length=200)

    def __str__(self):
        return self.parameter