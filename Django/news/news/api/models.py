from django.db import models
from django.utils import timezone

# Create your models here.

class Table(models.Model):
    Run_ID = models.CharField(max_length=120)
    Date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    Run_status = models.TextField()
    count = models.IntegerField()
    path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Run_ID)
