from django.db import models

# Create your models here.
class suggestion_model(models.Model):
    suggestion = models.CharField(max_length=240)

    def __str__(self):
        return suggestion
