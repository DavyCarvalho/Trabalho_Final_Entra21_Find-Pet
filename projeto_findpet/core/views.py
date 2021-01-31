from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet

@login_required(login_url='/login/')
def register_pet(request):
    return render(request, 'register_pet.html')


@login_required(login_url='/login/')
def set_pet(request):
    pet_name = request.POST.get('pet_name')
    district = request.POST.get('district')
    city = request.POST.get('city')
    contact_phone = request.POST.get('phone')
    contact_email = request.POST.get('email')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    user = request.user
    
    pet = Pet.objects.create(pet_name=pet_name, district=district, city=city, 
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
    pet = Pet.objects.filter(active=True)
    return render(request, 'list.html', {'pet':pet})


@login_required(login_url='/login/')
def list_user_pets(request):
    pet = Pet.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'pet':pet})


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
            return redirect('home')
        else:
            messages.error(request, 'Usuário e/ou Senha Inválidos!')
    return redirect('/login/')