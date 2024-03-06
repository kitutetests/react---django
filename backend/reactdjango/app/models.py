from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   name = models.CharField(max_length=100,null=True)
   other_name = models.CharField(max_length=100,null=True)
   id_number = models.CharField(max_length=8,null=True)
   email = models.EmailField(null=True)
   profile_picture = models.ImageField(upload_to='photo/' ,null=True ,blank=True)
   
   def __str__(self):
            return str(self.name)

class Property_for_renting(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    apartment_name = models.CharField( max_length=500,null=True)

    size_choices=(
        ('single room' , 'single room'),
        ('Double room' , 'Double room'),
        ('Bedsitter' , 'Bedsitter'),
        ('1 Bedroom' , '1 Bedroom'),
        ('2 Bedrooms' , '2 Bedrooms'),
        ('3 Bedrooms' , '3 Bedrooms'),
        ('4 Bedrooms' , '4 Bedrooms'),
        ('5 Bedrooms' , '5 Bedrooms'),
        ('Above 5 Bedrooms' , 'Above 5 Bedrooms'),
    )
    size = models.CharField(choices=size_choices , max_length=50)
    features= models.TextField()
    location = models.CharField(max_length=1000)
    pin_location = models.CharField(null=True,blank=True,default='Optional',max_length=1000)
    photos = models.ImageField(upload_to='images/' ,null=True)
    video = models.FileField(upload_to='videos/',blank=True, null=True) 
    price = models.IntegerField()
    deposit = models.IntegerField(null=True)
    id_photo_front = models.ImageField(upload_to='images/' ,null=True)
    id_photo_back = models.ImageField(upload_to='images/' ,null=True)
    water_fee = models.IntegerField(null=True)
    garbage_fee = models.IntegerField(null=True)
    landlord_contact = models.CharField(max_length=20,null=True)
    caretaker_contact = models.CharField(max_length=20,blank=True,null=True)
    agent_name =  models.CharField(max_length=2000,blank=True,null=True)
    agent_contact =  models.CharField(max_length=20,blank=True,null=True)
    posted = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True) 

    def __str__(self):
            return str(self.owner )

class Property_on_sale(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    choices=(
        ('Rentals' , 'Rentals'),
        ('Land' , 'Land'),
        ('House' , 'House'),
        ('Vehicle' , 'Vehicle'),
    )
    property_type = models.CharField(choices=choices , max_length=50)
    features= models.TextField()
    location = models.CharField(max_length=1000)
    pin_location = models.CharField(null=True,blank=True,max_length=1000)
    photos = models.ImageField(upload_to='images/' ,null=True)
    video = models.FileField(upload_to='videos/',  blank=True,null=True) 
    price = models.IntegerField()
    payment_process = models.TextField(null=True)
    contact = models.CharField(max_length=20) 
    posted = models.DateTimeField(auto_now=True)  
    is_available = models.BooleanField(default=True)  
    
    def __str__(self):
            return str(self.property_type)