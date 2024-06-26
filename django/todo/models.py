from django.db import models
from django.utils import timezone
 
 
class Todo(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title