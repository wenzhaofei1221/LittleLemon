from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest = models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self):
        return f"{self.name}"
        
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title}:{str(self.price)}"
    
    