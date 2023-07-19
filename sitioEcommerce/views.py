from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html', {
        'title':'Frontend Store'
    })


def login_view(request):
    if request.method == 'POST':
        #El metodo POST no es más que un diccionario
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Se ha iniciado sesión correctamente. Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')

    return render(request, 'users/login.html', {
        'title':'Login'
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Su sesión ha finalizado')
    return redirect('login')
