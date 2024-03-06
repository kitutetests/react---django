from django import forms

from .models import Property_for_renting,Property_on_sale

class HouseRentForm(forms.ModelForm):
   
    class Meta:
        model = Property_for_renting
        fields = ['size','apartment_name','location','pin_location','features','photos','video','price','deposit','water_fee','garbage_fee','landlord_contact','caretaker_contact','agent_name','agent_contact']
        widgets = {'pin_location': forms.TextInput(attrs={'placeholder':  '(optional)'}),
                 'landlord_contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
                 'caretaker_contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
                 'agent_contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
        }
    
class SellPropertyForm(forms.ModelForm):
   
    class Meta:
        model = Property_on_sale
        fields = ['property_type','features','location','pin_location','photos','video','price','payment_process','contact']
        widgets = {'pin_location': forms.TextInput(attrs={'placeholder': '(optional)'}),
                  'contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
                 
        }

  