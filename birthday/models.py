from django.db import models
from django.utils.timezone import now

class Birthday(models.Model):
    name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name