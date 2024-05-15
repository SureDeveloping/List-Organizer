from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ListTemplate(models.Model):
    list_owner = models.ForeignKey(User, on_delete=models.SET_NULL, 
    null=True, blank=True, related_name='owned_lists')
    list_title = models.CharField(max_length=200)
   
    def __str__(self):
        return self.list_title
