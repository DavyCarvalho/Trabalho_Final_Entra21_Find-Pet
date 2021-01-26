from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=30, default=None)
    district = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=100)
    description = models.TextField()
    contact_phone = models.CharField(max_length=11)
    contact_email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'pet'