from django.contrib.auth import login
from django.contrib.messages.context_processors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.backend import CustomBackend
from accounts.forms import CustomUserCreationForm, CustomLoginForm
from accounts.models import User
from notifications.models import Notification


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            confirmar_senha = form.cleaned_data['confirmar_senha']
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            endereco = form.cleaned_data['endereco']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']

            if senha == confirmar_senha:
                user = User(
                    usuario=usuario,
                    nome=nome,
                    cpf=cpf,
                    endereco=endereco,
                    telefone=telefone,
                    email=email,
                )
                user.set_password(senha)
                user.save()

                if usuario:
                    return redirect('logi')

                else:
                    print('invalid registration details')
            else:
                messages.error(request, 'Senhas não batem')

    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            backend1 = CustomBackend()
            user = backend1.authenticate_user(request, username=usuario, password=senha)
            print(user)
            if user:
                login(request, user, backend='accounts.backend.CustomBackend')
                return redirect('home')
            else:
                return HttpResponse('Usuário ou senha inválidos')
    else:
        form = CustomLoginForm()

    return render(request, 'registration/login.html', {'form': form})


def listar_notificacoes(request):
    user = request.user.id
    notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
    return render(request, 'assets/static/listar_notificacoes.html', {'notifications': notifications})