from django.db import models




class Menu(models.Model):
    
    Image = models.ImageField(upload_to="upload/images")
    Menu_Name = models.CharField(max_length=100)
    description = models.TextField()
    price  = models.IntegerField(default=0)
    
    
    
    