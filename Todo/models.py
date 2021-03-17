from django.db import models
from django.utils import timezone
# Create your models here.


class TodoModel(models.Model):
    text = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text