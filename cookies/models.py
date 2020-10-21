from django.db import models
from users.models import CustomUser

class Location(models.Model):
    name = models.CharField(max_length=128)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
