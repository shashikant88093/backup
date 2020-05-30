from django.db import models

# Create your models here.
class Table(models.Model):
    # username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Run_ID = models.CharField(max_length=120)
    Date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    Run_status = models.TextField()
    count = models.IntegerField()
    path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Run_ID)
        # return str(self.Run_status)

class Book(models.Model):
    title=models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length =256 , blank=True)
    price = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    is_published = models.BooleanField(default=False)
    published = models.DateField(blank= True, null=True, default=None)
    cover = models.ImageField(upload_to='cover/',blank=True)

    def __str__(self):
        return str(self.title)