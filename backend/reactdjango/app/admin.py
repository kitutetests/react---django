from django.contrib import admin
from . models import Profile,Property_for_renting,Property_on_sale,PropertyImage,Subscription,RentalSubscription
# Register your models here.

admin.site.register(PropertyImage)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','other_name','phone_number','email')

admin.site.register(Profile,ProfileAdmin)

class Property_on_rentAdmin(admin.ModelAdmin):
    list_display = ('owner' , 'id_number' , 'size','apartment_name','location')

    def id_number(self, obj):
        return obj.owner.id_number

admin.site.register(Property_for_renting,Property_on_rentAdmin)

class Property_on_saleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'property_type','location','contact')

admin.site.register(Property_on_sale,Property_on_saleAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('MpesaReceiptNumber','PhoneNumber','TransactionDate','valid_till')

admin.site.register(Subscription,SubscriptionAdmin)

class RentalSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('person','email','phone_number')

admin.site.register(RentalSubscription,RentalSubscriptionAdmin)