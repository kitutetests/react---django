from django.contrib import admin
from . models import Profile,Property_for_renting,Property_on_sale
# Register your models here.

admin.site.register(Profile)
admin.site.register(Property_on_sale)
admin.site.register(Property_for_renting)