from django import forms
from .models import Property_for_renting,Property_on_sale

class HouseRentForm(forms.ModelForm):
   
    class Meta:
        model = Property_for_renting
        fields = ['size','features','location','photos','video','price','contact']


    
class SellPropertyForm(forms.ModelForm):
   
    class Meta:
        model = Property_on_sale
        fields = ['property_type','features','location','photos','video','price','contact']


  