from django.urls import path
from .views import login_view, usuarios_view, home_view, logout_view, agregar_usuario_view,cambiar_estado_usuario, ver_usuario_view


urlpatterns = [
    path('iniciarSesion/', login_view, name='login'),
    path('usuarios/', usuarios_view, name='usuarios' ),
    path('agregar_usuario', agregar_usuario_view, name='agregar_usuario'),
    path('cambiar_estado_usuario/<int:user_id>/', cambiar_estado_usuario, name='cambiar_estado_usuario'),
    path('ver_usuario/<int:user_id>/', ver_usuario_view, name='ver_usuario'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout')
]