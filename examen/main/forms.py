from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='',max_length=25, widget=forms.TextInput(attrs={'placeholder':'Usuario'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Correo'}))
    first_name = forms.CharField(label='',max_length=25, widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    last_name = forms.CharField(label='',max_length=25, widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    password1 = forms.CharField(label='', max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(label='', max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Repita contraseña'})) 
    

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise ValidationError("El usuario ya existe")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email = email)
        if new.count():
             raise ValidationError("El correo ya existe")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("las contraseñas no coinciden")
        return password2
    

    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['password1']
        )
        return user
    
class ModificarUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'nuevo usuario'
        self.fields['first_name'].widget.attrs['placeholder'] = 'nuevo nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'nuevo apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'nuevo correo electrónico'