from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=30) #<----- default=None é o problema de aceitar valores vazios!
    pet_name = models.CharField(max_length=30)#<----- default=None é o problema de aceitar valores vazios!
    breed = models.CharField(max_length=15)#<----- default=None é o problema de aceitar valores vazios!
    district = models.CharField(max_length=50)#<----- default=None é o problema de aceitar valores vazios!
    city = models.CharField(max_length=100)
    description = models.TextField()#<----- default=None é o problema de aceitar valores vazios!
    contact_phone = models.CharField(max_length=11)
    contact_email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='uploaded_pet_photos')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'pet'
    
class EuVi(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30) #---------------------> USAR O USER QUE ESTÁ LOGADO no request !!!
    post = models.ForeignKey(Pet, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    description = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'core_eu_vi'

class HistoriasFelizes(models.Model):
    id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    description = models.TextField(default=None)

    def __str__(self):
        return str(self.id)
        
    class Meta:
        db_table = 'core_historiasfelizes'
