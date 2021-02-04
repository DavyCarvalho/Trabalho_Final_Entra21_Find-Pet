from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=30, default=None)
    pet_name = models.CharField(max_length=30, default=None)
    breed = models.CharField(max_length=15,default=None)
    district = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=100)
    description = models.TextField(default=None)
    contact_phone = models.CharField(max_length=11)
    contact_email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='uploaded_pet_photos')
    active = models.BooleanField(default=True)
    
    # eu_vi = models.ForeignKey(Eu_vi, default=None, on_delete=models.CASCADE) 
    
    # EM VEZ DE FAZER ISSO, FAZER UM FILTRO ONDE PET.ID == EU.POST !!!!!!!!
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'pet'
    
class Eu_vi(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30) #---------------------> USAR O USER QUE ESTÁ LOGADO no request !!!
    post = models.ForeignKey(Pet, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=30) #--------------------> USAR O USER QUE ESTÁ LOGADO no request !!!
    street = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    description = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    # class Meta:
    #     db_table = 'pet'
    #     pass
    


