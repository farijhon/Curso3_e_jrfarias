from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from inicio.models import Usuarios, Trabajador,Pais
from django.contrib import messages

# Create your views here.
def register(request):
    return render(request, 'register.html', {})
def inicioDef(request):
    return render(request, 'ini.html', {})
def paginaDef(request):
    return render(request,'pagina.html', {})
def loginSesionDef(request):
    if request.method == 'GET':
        return render(request, 'ini.html', {})
    else:
        usuarioStr = request.POST.get('userInTx')
        passwordStr= request.POST.get('passwordInPs')
        try:
             usuario= Usuarios.objects.get(usuario=usuarioStr, password=passwordStr)
             trabajadorList= Trabajador.objects.values()

             return render(request, "menu.html",{"list":trabajadorList,"usuarioStr": usuario.usuario})
        except Usuarios.DoesNotExist:
             return render(request, "ini.html", {"err":"Usuario o contraseña no son correctos"})
