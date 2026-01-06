from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

########################## Login  ###################################
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'app_cuentas/InicioDsesion.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'app_cuentas/InicioDsesion.html')

###################### Home ####################################
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home_view(request):
    return render(request, 'app_cuentas/Home.html')

#################### LOGOUT ###########################
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')


####################### Usuarios Ver ###############################

from django.contrib.auth.models import User
from django.shortcuts import render

@login_required(login_url='login')
def usuarios_view(request):
    usuarios = User.objects.all()
    return render(request, 'app_cuentas/usuarios.html', {
        'usuarios': usuarios
    })

####################### Usuarios Agregar ###############################

@login_required(login_url='login')
def agregar_usuario_view(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('usuarios')
    return render(request, 'app_cuentas/Agregar_usuario.html')

####################### Cambiar estado ###############################

from django.contrib.auth.decorators import user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)
def cambiar_estado_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    usuario.is_active = not usuario.is_active
    usuario.save()
    return redirect('usuarios')


####################### Ver usuario ###############################

from django.contrib.auth.decorators import user_passes_test

@login_required(login_url='login')
def ver_usuario_view(request, user_id):
    usuario = User.objects.get(id=user_id)
    return render(request, 'app_cuentas/Ver_usuario.html', {
        'usuario': usuario
    })

