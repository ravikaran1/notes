from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Note(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    timest=models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class querie(models.Model):
    sno1=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    issue=models.TextField()
    timest=models.DateTimeField(default=now)

    def __str__(self):
        return self.name

# Create your models here.
