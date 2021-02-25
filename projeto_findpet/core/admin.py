from django.contrib import admin
from .models import Pet, Eu_vi, ReportarPostagem

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'owner', 'pet_name', 'breed', 
                    'district', 'city', 'description', 
                    'contact_phone', 'contact_email', 
                    'begin_date', 'photo', 'active']
    
@admin.register(Eu_vi)
class Eu_viAdmin(admin.ModelAdmin):
    list_display = ['id','user','post', 'phone', 
                    'street', 'district', 'city', 
                    'description', 'begin_date']
    
    
@admin.register(ReportarPostagem)
class ReportarPostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'pet_id', 'pet_owner', 'pet_name', 'name', 
                    'contact_email', 'contact_phone', 'opcao']