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
                return redirect('usuarios')


            User.objects.create_user(username=username, email=email, password=password)
            messages.info(request, 'Usuario agregado exitosamente.')



            return redirect('usuarios')
        return redirect('usuarios')




####################### Cambiar estado ###############################

from django.contrib.auth.decorators import user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)
def cambiar_estado_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    usuario.is_active = not usuario.is_active
    usuario.save()
    messages.info(request, 'Estado del usuario cambiado correctamente.')
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


##########################################################################################################
## SECTOR ETB




####################### Usuarios Agregar Actualizado###############################
from .models import Usuario

@login_required(login_url='login')
def usuarios_view_actualizada(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app_cuentas/UsuarioEtb.html', {
        'usuarios': usuarios
    })




@login_required(login_url='login')
def agregar_usuario_actualizado(request):

    if request.method == 'POST':
        Usuario.objects.create(
            clasificacion=request.POST['clasificacion'],
            login=request.POST['login'],
            estado=request.POST['estado'],

            identificacion_usuario=request.POST['identificacion_usuario'],
            fecha_ingreso=request.POST['fecha_ingreso'],
            fecha_retiro=request.POST['fecha_retiro'],

            vicepresidente=request.POST['vicepresidente'],
            gerencia=request.POST['gerencia'],
            direccion=request.POST['direccion'],

            canal=request.POST['canal'],
            proveedor=request.POST['proveedor'],
            nro_contrato=request.POST['nro_contrato'],

            subcanal=request.POST['subcanal'],
            punto=request.POST['punto'],
            cc_supervisor=request.POST['cc_supervisor'],

            lider_etb=request.POST['lider_etb'],
            departamento=request.POST['departamento'],
            ciudad=request.POST['ciudad'],

            nombres=request.POST['nombres'],
            apellidos=request.POST['apellidos'],
            correo=request.POST['correo'],

            celular=request.POST['celular'],
            eps=request.POST['eps'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],

            sexo=request.POST['sexo'],
            cargo=request.POST['cargo'],
            perfil_portal_suma=request.POST['perfil_portal_suma'],

            restriccion=request.POST['restriccion'],
            causa_restriccion=request.POST['causa_restriccion'],
            id_fibra=request.POST['id_fibra'],

            fija=request.POST['fija'],
            movil=request.POST['movil'],
            id_cobre=request.POST['id_cobre'],
        )

        messages.success(request, 'Usuario agregado correctamente.')
        return redirect('usuarios_etb')

    return redirect('usuarios_etb')


    
login_required(login_url='login')
def buscar_usuario_view_actualizada(request):
    query = request.GET.get('buscador_Usuario', '')
    usuarios = Usuario.objects.filter(identificacion_usuario__icontains=query)
    if not usuarios.exists():
        messages.warning(request, 'No se encontraron usuarios que coincidan con la búsqueda.')

    else:
        messages.success(request, f'Se encontraron {usuarios.count()} usuarios que coinciden con la búsqueda.')
    

    return render(request, 'app_cuentas/UsuarioEtb.html', {
        'usuarios': usuarios,
        'query': query
    })


login_required(login_url='login')
def eliminar_usuario_actualizada(request, user_id):
    usuario = Usuario.objects.get(id=user_id)
    usuario.delete()
    messages.info(request, 'Usuario eliminado correctamente. ')
    return redirect('usuarios_etb')



@login_required(login_url='login')
def ver_usuario_view_actualizada(request, user_id):
    usuario = Usuario.objects.get(id=user_id)
    return render(request, 'app_cuentas/Ver_usuario_etb.html', {
        'usuario': usuario
    })

