from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from core.models import Pet, ReportarPostagem


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nome de Usuário (Usado para Acessar o Site)', max_length=50)
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        
class RegisterPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('owner', 'pet_name', 'breed', 'district', 'city', 'description', 'contact_phone',
                  'contact_email', 'photo')
        
class ReportarPostagemForm(forms.ModelForm):
    class Meta:
        model = ReportarPostagem
        fields = ['pet_id', 'pet_owner', 'pet_name', 'name', 
                    'contact_email', 'contact_phone', 'opcao']


# class EditUserForm(UserChangeForm):

#     class Meta(UserChangeForm.Meta):
#         username = forms.CharField(label='Nome de Usuário (Usado para Acessar o Site)', max_length=50)
#         first_name = forms.CharField(label='Nome')
#         last_name = forms.CharField(label='Sobrenome')
#         email = forms.EmailField()
        
#         model = User
#         fields = UserChangeForm.Meta.fields + ('Nome','nome','nome','noem')
    
#     # class Meta:
#     #     model = User
#     #     fields = ["username", "first_name", "last_name", "email"]
        
        
# class ResetPasswordForm(PasswordChangeForm):
    
#     password1 = forms.CharField()
#     password2 = forms.CharField()
    
#     pass
