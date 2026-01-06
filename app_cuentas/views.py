from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

########################### Manejo de Errores Handler         #############################

# core/views.py
from django.shortcuts import redirect

def redirect_404(request, exception):
    return redirect("login")  # o home / dashboard


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

            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe.')
                return render(request, 'app_cuentas/Agregar_usuario.html')


            User.objects.create_user(username=username, email=email, password=password)
            messages.info(request, 'Usuario agregado exitosamente.')



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


from django.contrib import messages


login_required(login_url='login')
def buscar_usuario_view(request):
    query = request.GET.get('buscador_Users', '')
    usuarios = User.objects.filter(username__icontains=query)
    if not usuarios.exists():
        messages.warning(request, 'No se encontraron usuarios que coincidan con la búsqueda.')

    else:
        messages.success(request, f'Se encontraron {usuarios.count()} usuarios que coinciden con la búsqueda.')
    

    return render(request, 'app_cuentas/Usuarios.html', {
        'usuarios': usuarios,
        'query': query
    })


login_required(login_url='login')
def eliminar_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    usuario.delete()
    messages.info(request, 'Usuario eliminado correctamente. ')
    return redirect('usuarios')