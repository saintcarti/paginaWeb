from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import UserProfile
from .forms import CustomUserCreationForm



def iniciosesion(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')
        
        user = authenticate(request, username= usuario , password= clave)

        if user is not None:
            profile = UserProfile.objects.get(user=user)

            request.session['perfil']= profile.role

            login(request, user)

            return redirect('inicio')
        else:
            context= {
                'error':'Error intente denuevo'
            }

            return render(request, 'registration/login.html', context)
        
    return render(request, 'registration/login.html')

def registro(request):
    data= {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            return redirect('inicio')
        

    return render(request, 'registration/register.html',data)

def exit(request):
    logout(request)
    return redirect('inicio')

def recuperar(request):
    return render(request, 'registration/recuperar.html')


def enviar_correo(request):
    send_mail(
        'prueba',
        'hecho con fines historicos',
        'tecuidosecu1234@gmail.com',
        ['amarocartescampos@gmail.com'],
        fail_silently=False,
    )
    return redirect('frame_correo')

def cargar_frame_correo(request):
    return render(request, 'tests/emailtest.html')

