from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   name = models.CharField(max_length=100,null=True)
   email = models.EmailField(null=True)
   
   def __str__(self):
            return str(self.name)

class Property_for_renting(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
   
    size_choices=(
        ('single room' , 'single room'),
        ('Double room' , 'Double room'),
        ('Bedsitter' , 'Bedsitter'),
        ('1 Bedroom' , '1 Bedroom'),
        ('2 Bedroom' , '2 Bedroom'),
        ('3 Bedroom' , '3 Bedroom'),
        ('Above 3 Bedroom' , 'Above 3 Bedroom'),
    )
    size = models.CharField(choices=size_choices , max_length=50)
    features= models.TextField()
    location = models.CharField(max_length=1000)
    photos = models.ImageField(upload_to='images/' ,null=True)
    video = models.FileField(upload_to='videos/', null=True) 
    price = models.IntegerField()
    contact = models.CharField(max_length=20) 
    posted = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True) 

    def __str__(self):
            return str(self.size )

class Property_on_sale(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    choices=(
        ('Rentals' , 'Rentals'),
        ('Land' , 'Land'),
        ('Home' , 'Home'),
    )
    property_type = models.CharField(choices=choices , max_length=50)
    features= models.TextField()
    location = models.CharField(max_length=1000)
    photos = models.ImageField(upload_to='images/' ,blank=True ,null=True)
    video = models.FileField(upload_to='videos/',  blank=True,null=True) 
    price = models.IntegerField()
    contact = models.CharField(max_length=20) 
    posted = models.DateTimeField(auto_now=True)  
    is_available = models.BooleanField(default=True)  
    
    def __str__(self):
            return str(self.property_type)