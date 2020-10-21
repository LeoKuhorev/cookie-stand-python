from django.db import models
from users.models import CustomUser

class Location(models.Model):
    name = models.CharField(max_length=128)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Location Manager')
    min_customers = models.IntegerField(help_text='Enter minimum number of customers')
    max_customers = models.IntegerField(help_text='Enter maximum number of customers')
    avg_sale = models.DecimalField(max_digits=5, decimal_places=2, help_text='Enter the average number of cookies per sale')
    
    def __str__(self):
        return self.name
    
class Cookie(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self):
        return self.name
