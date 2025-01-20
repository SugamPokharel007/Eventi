from django.db import models
from django.contrib.auth.models import User
from datetime import date, time

class ticketform(models.Model):
    DROPDOWN_CHOICES = [
        ('workshop', 'Workshop'),
        ('concert', 'Concert'),
        ('sports', 'Sports Event'),
        ('community', 'Community Events'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    quantity = models.PositiveIntegerField()
    dropdown_option = models.CharField(max_length=50, choices=DROPDOWN_CHOICES)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.name} - {self.dropdown_option} ({self.quantity})"
    
    
class contactform(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Concerts', 'Concerts'),
        ('Sports', 'Sports'),
        ('Workshop', 'Workshop'),
        ('Community', 'Community Events'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='events/')
    image2 = models.ImageField(upload_to='events/')
    event_date = models.DateField(default=date.today)  # Default to the current date
    event_time = models.TimeField(default=time(0, 0))  # Default to midnight
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.event_date} {self.event_time})"


