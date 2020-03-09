from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import Utilizador


class UserRegisterForm(forms.Form):
    name=forms.CharField(max_length=45,label="Nome")
    username=forms.CharField(max_length=45,label="username")
    email = forms.EmailField(max_length=45,label="Email")
    telefone=forms.CharField(max_length=45,label="Telefone/Telemovel")
    password1=forms.CharField(max_length=45,label="Password",widget=forms.PasswordInput())
    password2=forms.CharField(max_length=45,label="Password Confirm",widget=forms.PasswordInput())

    class Meta:
        model=Utilizador
        fields=['idutilizador','nome','email','telefone','password','username']
    
    def save(self):
        data = self.cleaned_data
        user=Utilizador(nome=data['name'],username=data['username'],
            email=data['email'],telefone=data['telefone'],password=data['password1'])
        user.save()
    
    def is_valid(self):
        data=self.cleaned_data
        #if(data[])