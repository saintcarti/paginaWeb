from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  exit,iniciosesion, recuperar, registro, enviar_correo,cargar_frame_correo
urlpatterns = [
    path('logout/', exit, name='logout'),
    path('login/', iniciosesion, name='login'),
    path('recuperar/', recuperar, name='recuperar'),
    path('registro/', registro, name='registro'),
    path('cargar_frame_correo/', cargar_frame_correo, name='frame_correo'),
    path('cargar_frame_correo/enviarcorreo', enviar_correo, name='enviar_correo'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='restablecer_contrasena'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='restablecer_comtrasena_correcto'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='restablecer_contrasena_confirmar'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='restablecer_contrasena_completo'),
]
