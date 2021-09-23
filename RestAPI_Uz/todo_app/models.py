from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=150)
    descrption = models.TextField()

    def __str__(self) -> str:
        return self.title