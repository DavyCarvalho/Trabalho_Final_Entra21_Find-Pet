from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    CHOICES_BREED = (
        ("Basset", "Basset"),
        ("Beagle", "Beagle"),
        ("Boder Collie", "Boder Collie"),
        ("Boxer", "Boxer"),
        ("Buldog Francês", "Buldog Francês"),
        ("Buldog Inglês", "Bulldog Inglês"),
        ("Bull Terrier", "Bull Terrier"),
        ("Chow-Chow", "Chow-Chow"),
        ("Dachshund (Salsicha)", "Dachshund (Salsicha)"),
        ("Golden", "Golden"),
        ("Husky Siberiano", "Husky Siberiano"),
        ("Retriever", "Retriever"),
        ("Labrador", "Labrador"),
        ("Lhasa Apso", "Lhasa Apso"),
        ("Lulu da Pomerânia", "Lulu da Pomerânia"),
        ("Maltês", "Maltês"),
        ("Pastor Alemão", "Pastor Alemão"),
        ("Pinscher", "Pinscher"),
        ("Pit Bull", "Pit Bull"),
        ("Poodle", "Poodle"),
        ("Pug", "Pug"),
        ("Rottweiler", "Rottweiler"),
        ("Schnauzer", "Schnauzer"),
        ("Shih-Tzu", "Shih-Tzu"),
        ("Vira-Lata(SRD)", "Vira-Lata(SRD)"),
        ("Yorkshire", "Yorkshire"),
        ("Outros", "Outros"),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=30) #<----- default=None é o problema de aceitar valores vazios!
    pet_name = models.CharField(max_length=30)#<----- default=None é o problema de aceitar valores vazios!
    breed = models.CharField(choices= CHOICES_BREED, max_length=35)#<----- default=None é o problema de aceitar valores vazios!
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
    
class Eu_vi(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30) #---------------------> USAR O USER QUE ESTÁ LOGADO no request !!!
    post = models.ForeignKey(Pet, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=15, default='')
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    description = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'core_eu_vi'

class HistoriasFelizes(models.Model): #adicionar campo foto para 'foto com o pet'
    id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    description = models.TextField(default=None)
    happyphoto = models.ImageField(upload_to='uploaded_histories_photos', default=None)
    begin_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
        
    class Meta:
        db_table = 'core_historias_felizes'
        
        
class ReportarPostagem(models.Model):
    
    CHOICES_PROBLEM = (
        ("Este Animal não pertence a essa pessoa!", "Este Animal não pertence a essa pessoa!"),
        ("Esse Animal já foi encontrado", "Esse Animal já foi encontrado"),
        ("Essa postagem parace enganosa/fraudosa", "Essa postagem parace enganosa/fraudosa"),
        ("Outro Motivo (Favor citar o motivo no campo de texto abaixo)", "Outro Motivo (Favor citar o motivo no campo de texto abaixo)"),
    )

    id = models.AutoField(primary_key=True)
    pet_id = models.CharField(max_length=30) #-----> pegar o id do pet no request
    pet_owner = models.CharField(max_length=30) #-----> pegar o owner do pet no request
    pet_name = models.CharField(max_length=30) #-----> pegar o name do pet no request
    name = models.CharField(max_length=30, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.IntegerField(blank=True, null=True, default=0)
    opcao = models.CharField(choices= CHOICES_PROBLEM, max_length=70)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'postagens_reportadas'