from django import forms
from .models import Property_for_renting,Property_on_sale

class HouseRentForm(forms.ModelForm):
   
    class Meta:
        model = Property_for_renting
        fields = ['size','apartment_name','location','features','photos','video','price','deposit','water_fee','garbage_fee','landlord_contact','caretaker_contact','agent_name','agent_contact']


    
class SellPropertyForm(forms.ModelForm):
   
    class Meta:
        model = Property_on_sale
        fields = ['property_type','features','location','photos','video','price','payment_process','contact']


  