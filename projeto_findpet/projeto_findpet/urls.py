"""projeto_findpet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from register import views as rv
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('pet/all/', views.list_all_pets, name='all'),
    path('pet/notifications/', views.list_pets_eu_vi, name='notifications'),    
    path('pet/user/', views.list_user_pets, name='all_user_pets'),
    path('pet/detail/<id>/', views.pet_detail, name='pet_detail'),
    path('register_user/', rv.register, name='register_user'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='login/submit'),
    path('pet/register_eu_vi/', views.register_eu_vi, name='register_eu_vi'),
    path('pet/register_eu_vi/submit',views.set_eu_vi),
    path('pet/sucess_eu_vi/', views.sucess_eu_vi, name='sucess_eu_vi'),
    path('pet/register/',views.register_pet, name='register_pet'),
    path('pet/register/submit',views.set_pet),
    path('pet/delete/<id>/', views.delete_pet),
    path('logout/', views.logout_user, name='logout'),
    path('', RedirectView.as_view(url='pet/all/')),
    path('teste/',views.register_pet, name='teste'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
