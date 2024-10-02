from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length = 100)
    isComplete = models.BooleanField(default = False)
    date_created = models.DateTimeField('Created', auto_now_add = True)
    date_updated = models.DateTimeField('Updated', auto_now = True)

    def __str__(self):
        return self.name
    
