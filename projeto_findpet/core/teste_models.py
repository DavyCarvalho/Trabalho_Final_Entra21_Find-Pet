from django.db import models
from django.contrib.auth.models import User

class Eu_vi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    phone =  models.CharField(max_length=30)
    
    
    

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=30, default=None)
    pet_name = models.CharField(max_length=30, default=None)
    breed = models.CharField(max_length=15,default=None)
    district = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=100)
    description = models.TextField()
    contact_phone = models.CharField(max_length=11)
    contact_email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.ForeignKey()
    photo = models.ImageField(upload_to='uploaded_pet_photos')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'pet'

