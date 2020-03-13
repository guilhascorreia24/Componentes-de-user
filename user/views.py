from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Utilizador


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() and Utilizador.objects.filter(email=request.POST['email'], telefone=request.POST['telefone']).exists() is False:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registo feito com Sucesso!')
            return redirect('blog-home')
        else:
            error=False
            error1=False
            error2=False
            if Utilizador.objects.filter(email=request.POST['email'], telefone=request.POST['telefone']).exists():
                error="Email ja existe"
            if 1<len(request.POST['password1'])<6:
                error1="password muito curta"
            if request.POST['password1']!=request.POST['password2']:
                error2="Passwords nao coincidem"
            return render(request,'register.html',{'form':form,'error1':error,'error2':error1,'error3':error2})
    form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})
