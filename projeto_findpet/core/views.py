from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet, Eu_vi

@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id') #DUVIDAS O QUE ISSO ESTÁ FAZENDO EXATAMENTE! FALAR COM O PROFESSOR!!!!
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.user == request.user:
            return render(request, 'register_pet.html', {'pet':pet})
    return render(request, 'register_pet.html')


@login_required(login_url='/login/')
def set_pet(request):
    pet_id = request.POST.get('pet_id')
    user = request.user
    owner = request.POST.get('owner')
    pet_name = request.POST.get('pet_name')
    breed = request.POST.get('breed')
    district = request.POST.get('district')
    city = request.POST.get('city')
    contact_phone = request.POST.get('phone')
    contact_email = request.POST.get('email')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.owner = owner
            pet.pet_name = pet_name
            pet.breed = breed
            pet.email = contact_email
            pet.phone = contact_phone
            pet.city = city
            pet.description = description
            if photo:
                pet.photo = photo
            pet.save()
    else:
        pet = Pet.objects.create(owner=owner, pet_name=pet_name, breed=breed, district=district, city=city, 
                                contact_phone=contact_phone, contact_email=contact_email,
                                description=description, photo=photo, user=user)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)


@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/') 


def list_all_pets(request):
    pet = Pet.objects.filter(active=True).order_by('-begin_date')
    return render(request, 'list.html', {'pet':pet})


@login_required(login_url='/login/')
def list_user_pets(request):
    pet = Pet.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'pet':pet})

@login_required(login_url='/login/')
def list_pets_eu_vi(request):
    
    pets_qs = Pet.objects.filter(active=True, user=request.user)
    pets = []
    
    class PetComEu_vi():
        def __init__(self, pet_name, photo, begin_date,
                     user_eu_vi, phone_eu_vi, street_eu_vi,
                     district_eu_vi, city_eu_vi, 
                     description_eu_vi, begin_date_eu_vi):
            self.pet_name = pet_name
            self.photo = photo
            self.begin_date = begin_date
            self.user_eu_vi = user_eu_vi
            self.phone_eu_vi = phone_eu_vi
            self.street_eu_vi = street_eu_vi
            self.district_eu_vi = district_eu_vi
            self.city_eu_vi = city_eu_vi
            self.description_eu_vi = description_eu_vi
            self.begin_date_eu_vi = begin_date_eu_vi 
    
    for pet in pets_qs:
        
        UltimoQueViu = Eu_vi.objects.filter(post=pet.id).order_by('-begin_date')[0]
        
        petComUltimoQueViu = PetComEu_vi(
            
            pet_name = pet.pet_name,
            photo = pet.photo,
            begin_date = pet.begin_date,
            user_eu_vi = UltimoQueViu.user,
            phone_eu_vi = UltimoQueViu.phone,
            street_eu_vi = UltimoQueViu.street,
            district_eu_vi = UltimoQueViu.district,
            city_eu_vi = UltimoQueViu.city,
            description_eu_vi = UltimoQueViu.description,
            begin_date_eu_vi =  UltimoQueViu.begin_date    
        )
        
        pets.append(petComUltimoQueViu)
        
    return render(request, 'notifications.html', {'pets':pets})


def pet_detail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request, 'pet.html', {'pet':pet})


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/login/') 


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all')
        else:
            messages.error(request, 'Usuário e/ou Senha Inválidos!')
    return redirect('/login/')