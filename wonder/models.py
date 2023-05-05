from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.
class Evento(models.Model):
    created_by = models.ForeignKey(User, related_name='psicologo', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
