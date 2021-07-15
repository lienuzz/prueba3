from core.models import categoria, Pintura
from django.shortcuts import render, redirect
from core.forms import PinturaForm


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def form_pinturas(request):
    datos = {
        'form':PinturaForm
    }
    #CREATE 
    if request.method == 'POST':
        #PinturaForm(request.POST) esta linea RECIBE TODOS LOS DATOS DEL FORMULARIO
        formulario = PinturaForm(request.POST)
        # .is_valid PREGUNTA SI CUMPLE CON LOS REQUISITOS DEL MODELO EN MODELS.PY
        if formulario.is_valid:
            #insert de django
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request,'core/form_pinturas.html', datos)

def Pinturas(request):
    #READ
    #select * from vehiculo;
    pintura = Pintura.objects.all()
    datos = {
        "pintura": pintura
    }
    return render(request, "core/pinturas.html",datos)

def form_mod_pinturas(request, id):
    #UPDATE
    #Pintura.objects.get(patente = id) ESTO ES UN SELECT CON WHERE DESDE FORMULARIO
    pintura = Pintura.objects.get(idPintura = id)
    datos = {
        "form":PinturaForm(instance= pintura)
    }

    if request.method == 'POST':
        #PinturaForm(request.POST) esta linea RECIBE TODOS LOS DATOS DEL FORMULARIO
        formulario = PinturaForm(data = request.POST, instance = pintura)
        # .is_valid PREGUNTA SI CUMPLE CON LOS REQUISITOS DEL MODELO EN MODELS.PY
        if formulario.is_valid:
            #insert de django
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request,'core/form_mod_pinturas.html', datos)

def form_del_pinturas(request,id):
    pintura = Pintura.objects.get(idPintura= id)
    #DELETE
    pintura.delete()
    return redirect(to="/pinturas/")

