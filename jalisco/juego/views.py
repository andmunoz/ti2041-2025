from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        numero = int(request.POST.get('numero'))
        if numero >= 1 and numero <= 100: 
            ganador = numero + 1
            context = { 
                'respuesta': 'Te gano con el ' + str(ganador) 
            }
        else:
            context = { 
                'respuesta': 'No hagas trampa' 
            }
    return render(request, 'home.html', context)
