import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a', 'Admin'),
        ('u', 'User'),
    )
    roles = models.CharField(max_length=1, choices=ROLE_CHOICES)



class TodoModel(models.Model):
    task = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
        return self.task

    class Meta:
        db_table = 'TODO_List'
