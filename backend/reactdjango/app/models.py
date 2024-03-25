from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   name = models.CharField(max_length=100,null=True)
   other_name = models.CharField(max_length=100,null=True)
   id_number = models.CharField(max_length=8,null=True)
   phone_number = models.CharField(max_length=13,null=True)
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
    pin_location = models.CharField(null=True,blank=True,max_length=1000)
    main_image = models.ImageField(upload_to='images/' ,null=True)
    video = models.FileField(upload_to='videos/',blank=True, null=True) 
    price = models.IntegerField()
    deposit = models.IntegerField(null=True,default=0)
    water_fee = models.CharField(max_length=200,default=0,null=True)
    garbage_fee = models.CharField(max_length=200,default=0,null=True)
    landlord_contact = models.CharField(max_length=20,null=True)
    caretaker_contact = models.CharField(max_length=20,blank=True,null=True)
    agent_name =  models.CharField(max_length=2000,blank=True,null=True)
    agent_contact =  models.CharField(max_length=20,blank=True,null=True)
    id_photo_front = models.ImageField(upload_to='images/' ,null=True)
    id_photo_back = models.ImageField(upload_to='images/' ,null=True)
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
    main_photo = models.ImageField(upload_to='images/' ,null=True)
    video = models.FileField(upload_to='videos/',  blank=True,null=True) 
    price = models.IntegerField()
    deposit = models.IntegerField(null=True,default=0)
    payment_process = models.TextField(null=True)
    contact = models.CharField(max_length=20) 
    id_photo_front = models.ImageField(upload_to='images/' ,null=True)
    id_photo_back = models.ImageField(upload_to='images/' ,null=True)
    posted = models.DateTimeField(auto_now=True)  
    is_available = models.BooleanField(default=True)  
    
    def __str__(self):
            return str(self.property_type)  + str(self.contact)
    

class PropertyImage(models.Model):
    property_renting = models.ForeignKey(Property_for_renting, on_delete=models.CASCADE, related_name='rental_photos',null=True)
    property_on_sale = models.ForeignKey(Property_on_sale, on_delete=models.CASCADE, related_name='property_on_photos',null=True)
    image = models.ImageField(upload_to='images/')


class Subscription(models.Model):
    # person = models.ForeignKey(Profile,on_delete=models.CASCADE)
    CheckoutRequestID = models.CharField(max_length=50, blank=True, null=True)
    MerchantRequestID = models.CharField(max_length=20, blank=True, null=True)
    ResultCode = models.IntegerField(blank=True, null=True)
    ResultDesc = models.CharField(max_length=120, blank=True, null=True)
    Amount = models.FloatField(blank=True, null=True)
    MpesaReceiptNumber = models.CharField(max_length=15, blank=True, null=True)
    TransactionDate = models.DateTimeField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=13, blank=True, null=True)
    valid_till = models.DateTimeField()


    
