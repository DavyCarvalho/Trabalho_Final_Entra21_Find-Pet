from django.contrib import admin
from .models import Pet, EuVi

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'owner', 'pet_name', 'breed', 
                    'district', 'city', 'description', 
                    'contact_phone', 'contact_email', 
                    'begin_date', 'photo', 'active']
    
@admin.register(EuVi)
class Eu_viAdmin(admin.ModelAdmin):
    list_display = ['id','user','post', 'phone', 
                    'street', 'district', 'city', 
                    'description', 'begin_date']