from django import forms

from .models import Property_for_renting,Property_on_sale,Profile,PropertyImage
class ProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = ['profile_picture']


class HouseRentForm(forms.ModelForm):
   
    class Meta:
        model = Property_for_renting
        fields = ['size','apartment_name','location','pin_location','features','main_image','video','price','deposit','water_fee','garbage_fee','landlord_contact','caretaker_contact','agent_name','agent_contact','id_photo_front','id_photo_back']

        widgets = {'pin_location': forms.TextInput(attrs={'placeholder':  '(optional)'}),
                 'landlord_contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
                 'caretaker_contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
                 'agent_contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
        }
    
class SellPropertyForm(forms.ModelForm):
   
    class Meta:
        model = Property_on_sale
        fields = ['property_type','features','location','pin_location','photos','video','price','deposit','payment_process','contact','id_photo_front','id_photo_back']
        widgets = {'pin_location': forms.TextInput(attrs={'placeholder': '(optional)'}),
                  'contact': forms.TextInput(attrs={'placeholder':  '+2547XXXXXXXX'}),
                 
        }

  