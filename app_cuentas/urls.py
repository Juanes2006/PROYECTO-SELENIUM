from django.urls import path
from app_cuentas.views import login_view, usuarios_view, home_view, logout_view, agregar_usuario_view,cambiar_estado_usuario, ver_usuario_view, buscar_usuario_view, eliminar_usuario,agregar_usuario_actualizado,usuarios_view_actualizada, usuarios_view_actualizada, buscar_usuario_view_actualizada, eliminar_usuario_actualizada, ver_usuario_view_actualizada
urlpatterns = [

    path('iniciarSesion/', login_view, name='login'),
    path('usuarios/', usuarios_view, name='usuarios' ),
    path('buscar_usuario/', buscar_usuario_view, name='buscar_usuario' ),

    path('agregar_usuario', agregar_usuario_view, name='agregar_usuario'),
    ###############
    # agregar usuario actualizado
    path('usuarios_etb/', usuarios_view_actualizada, name='usuarios_etb'),
    path('agregar_usuario_actualizado/', agregar_usuario_actualizado, name='agregar_usuario_actualizado'),
    path('buscar_usuario_etb/', buscar_usuario_view_actualizada, name='buscar_usuario_etb' ),
    path('eliminar_usuario_etb/<int:user_id>', eliminar_usuario_actualizada, name='eliminar_usuario_etb'),
    path('ver_usuario_etb/<int:user_id>/', ver_usuario_view_actualizada, name='ver_usuario_etb'),
    

    ###############
    path('cambiar_estado_usuario/<int:user_id>/', cambiar_estado_usuario, name='cambiar_estado_usuario'),
    path('ver_usuario/<int:user_id>/', ver_usuario_view, name='ver_usuario'),
    path('eliminar_usuario/<int:user_id>', eliminar_usuario, name='eliminar_usuario'),

    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout')
]