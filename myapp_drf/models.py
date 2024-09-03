from django.db import models

# Create your models here.
class student(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name