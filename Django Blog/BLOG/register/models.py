from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#for uploading files to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class tasks(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    date_assigned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
