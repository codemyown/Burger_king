from django.db import models





class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Phone_No = models.IntegerField(default=0)
    Email = models.CharField(max_length=50)
    Persons = models.IntegerField(default='')
    date = models.DateField()
    
    